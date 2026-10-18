import csv
import os

from src import calculator

# path to the csv file in the data folder
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "student_scores.csv")

# how much each part counts toward the final grade
HOMEWORK_WEIGHT = 0.3
MIDTERM_WEIGHT = 0.3
FINAL_WEIGHT = 0.4


def load_scores(file_path=DATA_FILE):
    """
    Reads the student scores csv file.
    Args:
        file_path (str): Path to the csv file.
    Returns:
        list: List of dictionaries, one for each student.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Could not find file: " + file_path)

    students = []
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = {
                "name": row["name"],
                "homework": float(row["homework"]),
                "midterm": float(row["midterm"]),
                "final": float(row["final"]),
            }
            students.append(student)
    return students


def weighted_score(homework, midterm, final):
    """
    Calculates the weighted score for one student.
    Args:
        homework (int/float): Homework score out of 100.
        midterm (int/float): Midterm score out of 100.
        final (int/float): Final exam score out of 100.
    Returns:
        float: Weighted score rounded to 2 decimals.
    Raises:
        ValueError: If a score is not a number or not between 0 and 100.
    """
    for score in [homework, midterm, final]:
        if not isinstance(score, (int, float)):
            raise ValueError("Scores must be numbers.")
        if score < 0 or score > 100:
            raise ValueError("Scores must be between 0 and 100.")

    # using the calculator functions from the original lab
    hw_part = calculator.fun3(homework, HOMEWORK_WEIGHT)
    mid_part = calculator.fun3(midterm, MIDTERM_WEIGHT)
    final_part = calculator.fun3(final, FINAL_WEIGHT)
    total = calculator.fun4(hw_part, mid_part, final_part)

    # rounding because floats can give things like 89.99999
    return round(total, 2)


def letter_grade(score):
    """
    Converts a number score to a letter grade.
    Args:
        score (int/float): Score out of 100.
    Returns:
        str: Letter grade A, B, C, D or F.
    Raises:
        ValueError: If score is not a number.
    """
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def class_summary(students):
    """
    Gets summary stats for the whole class.
    Args:
        students (list): List of student dictionaries from load_scores.
    Returns:
        dict: Number of students, average, highest, lowest and grade counts.
    Raises:
        ValueError: If the student list is empty.
    """
    if len(students) == 0:
        raise ValueError("Student list is empty.")

    final_scores = []
    for s in students:
        score = weighted_score(s["homework"], s["midterm"], s["final"])
        final_scores.append(score)

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in final_scores:
        grade = letter_grade(score)
        grade_counts[grade] += 1

    summary = {
        "num_students": len(final_scores),
        "average": round(calculator.fun7(final_scores), 2),
        "highest": max(final_scores),
        "lowest": min(final_scores),
        "grade_counts": grade_counts,
    }
    return summary


if __name__ == "__main__":
    students = load_scores()

    print("Student Grade Report")
    print("====================")
    for s in students:
        score = weighted_score(s["homework"], s["midterm"], s["final"])
        print(f"{s['name']:<10} {score:>6}   {letter_grade(score)}")

    summary = class_summary(students)
    print()
    print("Class Summary")
    print("=============")
    print("Students:", summary["num_students"])
    print("Average:", summary["average"])
    print("Highest:", summary["highest"])
    print("Lowest:", summary["lowest"])
    print("Grade counts:", summary["grade_counts"])
