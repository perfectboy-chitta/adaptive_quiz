
import matplotlib.pyplot as plt

def plot_accuracy(accuracy_by_diff):
    levels = ["Easy", "Medium", "Hard"]
    # Ensure all keys exist and get the accuracy values in the correct order
    accuracies = [
        accuracy_by_diff.get('easy', 0),
        accuracy_by_diff.get('medium', 0),
        accuracy_by_diff.get('hard', 0)
    ]

    plt.figure(figsize=(8, 5)) # Create a new figure for the plot
    plt.plot(levels, accuracies, marker='o', linestyle='-', color='b')

    # Adding titles and labels for clarity
    plt.title("Your Accuracy by Difficulty Level")
    plt.xlabel("Difficulty Level")
    plt.ylabel("Accuracy (%)")
    plt.ylim(0, 105) # Set y-axis limit from 0 to 105 for better padding
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout() # Adjust layout to make room for labels

    # Display the plot
    print("📊 Displaying your performance graph...")
    plt.show()
