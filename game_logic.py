from config import TOTAL_QUESTIONS

def get_next_difficulty(current_difficulty, is_correct):
    """Determines the next difficulty level based on the current one and the player's answer.

    Args:
        current_difficulty (str): The current difficulty level.
        is_correct (bool): True if the player answered correctly, False otherwise.

    Returns:
        str: The next difficulty level.
    """
    if is_correct:
        if current_difficulty == "easy":
            return "medium"
        elif current_difficulty == "medium":
            return "hard"
        else:
            return "hard" 
    else:
        if current_difficulty == "hard":
            return "medium"
        elif current_difficulty == "medium":
            return "easy"
        else:
            return "easy" 

def intelligence_rating(score, difficulty_history):
    """Calculates a fun "Intelligence Rating" based on performance.

    Args:
        score (int): The player's final score.
        difficulty_history (list): A list of the difficulty levels faced.

    Returns:
        str: A string containing the player's rating.
    """
    if score <= max(1, TOTAL_QUESTIONS // 3):
        return "Beginner Thinker 🧩"
    elif score <= max(2, (TOTAL_QUESTIONS * 2) // 3):
        return "Smart Learner 📘"
    else:
        if difficulty_history.count("hard") >= max(1, TOTAL_QUESTIONS // 3):
            return "Data Genius 🧠🚀"
        return "Intelligent Mind 🔍"

def calculate_accuracy_stats(stats):
    """Calculates the accuracy percentage for each difficulty level.

    Args:
        stats (dict): A dictionary tracking questions asked and answered correctly.

    Returns:
        dict: A dictionary mapping difficulty to accuracy percentage.
    """
    accuracy_by_diff = {}
    for diff_level in ["easy", "medium", "hard"]:
        asked = stats[diff_level]["asked"]
        correct = stats[diff_level]["correct"]
        # Avoid division by zero
        percentage = int(round((correct / asked) * 100)) if asked > 0 else 0
        accuracy_by_diff[diff_level] = percentage
    return accuracy_by_diff
