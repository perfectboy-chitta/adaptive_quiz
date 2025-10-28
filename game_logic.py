from config import TOTAL_QUESTIONS

def get_next_difficulty(current_difficulty, is_correct):
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
    if score <= max(1, TOTAL_QUESTIONS // 3):
        return "Beginner Thinker 🧩"
    elif score <= max(2, (TOTAL_QUESTIONS * 2) // 3):
        return "Smart Learner 📘"
    else:
        if difficulty_history.count("hard") >= max(1, TOTAL_QUESTIONS // 3):
            return "Data Genius 🧠🚀"
        return "Intelligent Mind 🔍"

def calculate_accuracy_stats(stats):
    accuracy_by_diff = {}
    for diff_level in ["easy", "medium", "hard"]:
        asked = stats[diff_level]["asked"]
        correct = stats[diff_level]["correct"]
        # Avoid division by zero
        percentage = int(round((correct / asked) * 100)) if asked > 0 else 0
        accuracy_by_diff[diff_level] = percentage
    return accuracy_by_diff
