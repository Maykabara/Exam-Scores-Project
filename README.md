# Generating Exam Scores

This project simulates and visualizes exam scores for a class of students across multiple subjects. It demonstrates how to generate random data, process it using Python, and create insightful visualizations using data visualization libraries.

---

## Features

- Simulates exam scores for a configurable number of students and subjects.
- Generates random scores within a specified range (e.g., 0–100).
- Calculates statistical insights like averages, highest/lowest scores, and pass/fail rates.
- Visualizes the data using:
  - Bar charts (student performance by subject).
  - Pie charts (pass/fail ratios).
  - Line graphs (score trends across subjects).

---

## Technologies Used

- **Python**: The core programming language for data generation and processing.
- **NumPy**: For generating random exam scores.
- **Pandas**: For organizing data into a structured format.
- **Matplotlib**: For visualizing data with charts and graphs.
- **Seaborn** (Optional): For advanced and aesthetically pleasing visualizations.

---

## Project Structure
exam-scores/ 
│ 
├── main.py # Main script to run the project 
├── requirements.txt # List of dependencies 
├── README.md # Project documentation 
└── output/ # Directory for saving generated visualizations



---

## How It Works

1. **Data Generation**:
   - Simulates random scores for a specified number of students and subjects.
   - Scores are generated using NumPy and stored in a Pandas DataFrame.

2. **Data Processing**:
   - Calculates the average, minimum, and maximum scores for each subject.
   - Computes pass/fail statistics based on a threshold (e.g., 50% to pass).

3. **Visualization**:
   - Bar charts: Show performance of students by subject.
   - Pie charts: Highlight pass/fail ratios for each subject.
   - Line graphs: Display trends in scores across subjects.

---

## How to Run

 **Clone the Repository**:
   ```bash
   git clone https://github.com/Maykabara/Exam-Scores-Project.git
   cd Exam-Scores-Project
