import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time

# Configuration
NUM_STUDENTS = 30  # Number of students
NUM_SUBJECTS = 5   # Number of subjects
SCORE_MIN = 0      # Minimum score
SCORE_MAX = 100    # Maximum score
PASS_THRESHOLD = 50  # Pass mark

SUBJECTS = [f"Subject {i+1}" for i in range(NUM_SUBJECTS)]
STUDENT_NAMES = [f"Student {i+1}" for i in range(NUM_STUDENTS)]


def generate_scores(num_students, num_subjects, score_min, score_max):
    """
    Generates random exam scores for students across subjects.
    """
    scores = np.random.randint(score_min, score_max + 1, (num_students, num_subjects))
    return pd.DataFrame(scores, columns=SUBJECTS, index=STUDENT_NAMES)


def calculate_statistics(scores_df):
    """
    Calculates statistics for the scores: averages, min, max, and pass rates.
    """
    stats = {
        "Average Score": scores_df.mean(),
        "Minimum Score": scores_df.min(),
        "Maximum Score": scores_df.max(),
        "Pass Rate (%)": (scores_df[scores_df >= PASS_THRESHOLD].count() / len(scores_df) * 100),
    }
    return stats


def visualize_data(scores_df, stats):
    """
    Creates and saves visualizations for the exam scores and statistics.
    """
    os.makedirs("output", exist_ok=True)  # Ensure the output directory exists

    # Bar Chart: Student scores in the first subject
    scores_df.iloc[:, 0].plot(kind="bar", figsize=(10, 5), color="skyblue")
    plt.title(f"Scores of Students in {scores_df.columns[0]}")
    plt.ylabel("Score")
    plt.xlabel("Students")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/bar_chart_scores.png")
    plt.close()

    # Pie Chart: Pass/Fail ratio for the first subject
    pass_count = scores_df[scores_df.iloc[:, 0] >= PASS_THRESHOLD].count()[0]
    fail_count = len(scores_df) - pass_count
    plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%", colors=["green", "red"])
    plt.title(f"Pass/Fail Ratio in {scores_df.columns[0]}")
    plt.savefig("output/pie_chart_pass_fail.png")
    plt.close()

    # Line Graph: Average scores across subjects
    stats["Average Score"].plot(kind="line", marker="o", figsize=(8, 5), color="orange")
    plt.title("Average Scores Across Subjects")
    plt.ylabel("Average Score")
    plt.xlabel("Subjects")
    plt.xticks(range(len(SUBJECTS)), SUBJECTS)
    plt.grid()
    plt.tight_layout()
    plt.savefig("output/line_graph_avg_scores.png")
    plt.close()


def main():
    """
    Main function to run the project.
    """
    print("Generating exam scores... Please wait...\n")
    
    # Step 1: Generate Scores
    scores_df = generate_scores(NUM_STUDENTS, NUM_SUBJECTS, SCORE_MIN, SCORE_MAX)

    # Real-time update: Show the generated scores
    print("Exam Scores (Generated for each student):")
    print(scores_df)
    print("\nProcessing statistics...\n")

    # Step 2: Calculate Statistics
    stats = calculate_statistics(scores_df)

    # Real-time update: Show the statistics
    print("Statistics:")
    time.sleep(1)
    print(f"Average Score per Subject:\n{stats['Average Score']}")
    print(f"\nMinimum Score per Subject:\n{stats['Minimum Score']}")
    print(f"\nMaximum Score per Subject:\n{stats['Maximum Score']}")
    print(f"\nPass Rate (%) per Subject:\n{stats['Pass Rate (%)']}")
    print("\nVisualizing data...\n")

    # Step 3: Visualize Data
    visualize_data(scores_df, stats)

    # Step 4: Save Results
    scores_df.to_csv("output/scores.csv")
    
    # Real-time update: Confirm the save
    print("Results and visualizations have been saved in the 'output/' folder.\n")
    print("Process completed!")

if __name__ == "__main__":
    main()
