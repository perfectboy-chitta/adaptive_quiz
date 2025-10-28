import requests
import random
import html
import time
from config import API_CATEGORY_URL, API_QUESTION_URL, RETRY_FETCHES, API_TIMEOUT

def get_categories():
    try:
        response = requests.get(API_CATEGORY_URL, timeout=API_TIMEOUT)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        # Create a dictionary of {id: name} from the API response
        categories = {cat['id']: cat['name'] for cat in data.get('trivia_categories', [])}
        return categories
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Could not fetch categories from API: {e}")
        print("Falling back to a basic list of categories.")
        return {9: "General Knowledge", 17: "Science & Nature", 23: "History"}

def fetch_question(difficulty, category_id):
    params = {
        "amount": 1,
        "difficulty": difficulty,
        "type": "multiple",
        "category": category_id
    }

    for attempt in range(RETRY_FETCHES):
        try:
            response = requests.get(API_QUESTION_URL, params=params, timeout=API_TIMEOUT)
            response.raise_for_status()
            data = response.json()

            # The API returns response_code 0 for success.
            if data.get('response_code') != 0 or not data.get('results'):
                # This can happen if there are no questions for the specific combo
                return None, None, None

            question_data = data['results'][0]
            question = html.unescape(question_data['question'])
            correct_answer = html.unescape(question_data['correct_answer'])
            incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]

            options = incorrect_answers + [correct_answer]
            random.shuffle(options)

            return question, correct_answer, options

        except requests.exceptions.RequestException:
            # Wait a moment before the next attempt
            time.sleep(0.5)
            continue

    # If all retries fail, return None
    return None, None, None
