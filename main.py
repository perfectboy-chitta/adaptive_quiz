
from config import TOTAL_QUESTIONS
from quiz_api import get_categories, fetch_question
from game_logic import get_next_difficulty, intelligence_rating, calculate_accuracy_stats
from plotter import plot_accuracy

def print_intro():
    print("===============================================")
    print("        Where Data Meets Intelligence")
    print("===============================================")
    print("Welcome to the Adaptive Intelligence Quiz Game!")
    print("This quiz adapts its difficulty based on your answers.\n")

def select_category(categories):
    print("Available categories (ID : Name):")
    for cat_id, name in sorted(categories.items()):
        print(f"{cat_id}: {name}")

    while True:
        try:
            choice_id = int(input("\nEnter the Category ID you want to play: ").strip())
            if choice_id in categories:
                print(f"You selected: {categories[choice_id]}\n")
                return choice_id, categories[choice_id]
            else:
                print("Invalid Category ID. Please choose one from the list above.")
        except ValueError:
            print("Please enter a valid number for the Category ID.")

def adaptive_quiz():
    print_intro()
    categories = get_categories()
    category_id, _ = select_category(categories)

    # --- Initialize Tracking Variables ---
    score = 0
    difficulty = "medium"  # Start at medium
    difficulty_history = ["medium"] # Log the starting difficulty
    stats = {
        "easy": {"asked": 0, "correct": 0},
        "medium": {"asked": 0, "correct": 0},
        "hard": {"asked": 0, "correct": 0}
    }

    print(f"Starting quiz of {TOTAL_QUESTIONS} questions. Good luck!\n")

    for i in range(TOTAL_QUESTIONS):
        print(f"Question {i+1} — Current difficulty: {difficulty.upper()}")
        q, correct_ans, options = fetch_question(difficulty, category_id)

        if q is None:
            print("⚠️  Couldn't fetch a question for this difficulty/category. Skipping.\n")
            continue

        stats[difficulty]["asked"] += 1
        print(q)
        for idx, opt in enumerate(options, start=1):
            print(f"  {idx}. {opt}")

        # --- Get and check user's answer ---
        try:
            ans_idx = int(input("Enter your answer (1-4): ").strip())
            user_answer = options[ans_idx - 1]
        except (ValueError, IndexError):
            print("❌ Invalid input — this will be counted as incorrect.")
            user_answer = None

        is_correct = user_answer and user_answer.strip().lower() == correct_ans.strip().lower()

        if is_correct:
            print("✅ Correct!")
            score += 1
            stats[difficulty]["correct"] += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {correct_ans}")

        difficulty = get_next_difficulty(difficulty, is_correct)
        difficulty_history.append(difficulty)
        print("-" * 40)

    accuracy_by_diff = calculate_accuracy_stats(stats)
    rating = intelligence_rating(score, difficulty_history)

    print("\n========== Quiz Summary ==========")
    print(f"Total Score: {score} / {TOTAL_QUESTIONS}")
    print(f"Difficulty Trend: {' → '.join(d.title() for d in difficulty_history)}")
    print("\nAccuracy by difficulty:")
    for d in ["easy", "medium", "hard"]:
        print(f"  {d.title():6s}: {stats[d]['correct']} / {stats[d]['asked']}  -> {accuracy_by_diff[d]}%")

    print(f"\nYour Intelligence Level: {rating}")
    print("==================================\n")

    plot_accuracy(accuracy_by_diff)

if __name__ == "__main__":
    adaptive_quiz()
