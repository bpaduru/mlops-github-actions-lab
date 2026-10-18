import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator
from src import grade_stats


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun4_bad_input(self):
        with self.assertRaises(ValueError):
            calculator.fun4(1, 2, "3")

    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5)
        self.assertEqual(calculator.fun5(7, 2), 3.5)
        self.assertEqual(calculator.fun5(-8, 2), -4)

    def test_fun5_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(10, 0)

    def test_fun6(self):
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 0), 1)
        self.assertEqual(calculator.fun6(9, 0.5), 3)

    def test_fun7(self):
        self.assertEqual(calculator.fun7([1, 2, 3]), 2)
        self.assertEqual(calculator.fun7([-5, 5]), 0)
        self.assertAlmostEqual(calculator.fun7([0.1, 0.2]), 0.15)

    def test_fun7_bad_input(self):
        with self.assertRaises(ValueError):
            calculator.fun7([])
        with self.assertRaises(ValueError):
            calculator.fun7([1, "two"])

    def test_strings_not_allowed(self):
        # using subTest so it shows which function failed
        for func in [calculator.fun1, calculator.fun2, calculator.fun3, calculator.fun5, calculator.fun6]:
            with self.subTest(func=func.__name__):
                with self.assertRaises(ValueError):
                    func("a", 2)


class TestGradeStats(unittest.TestCase):

    def setUp(self):
        # load the data once before each test
        self.students = grade_stats.load_scores()

    def test_load_scores(self):
        self.assertEqual(len(self.students), 10)
        self.assertEqual(self.students[0]["name"], "Alex")
        self.assertIsInstance(self.students[0]["homework"], float)

    def test_load_scores_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            grade_stats.load_scores("not_a_real_file.csv")

    def test_weighted_score(self):
        self.assertEqual(grade_stats.weighted_score(100, 100, 100), 100)
        self.assertEqual(grade_stats.weighted_score(80, 70, 90), 81)

    def test_weighted_score_out_of_range(self):
        with self.assertRaises(ValueError):
            grade_stats.weighted_score(101, 80, 80)
        with self.assertRaises(ValueError):
            grade_stats.weighted_score(80, -1, 80)

    def test_letter_grade(self):
        self.assertEqual(grade_stats.letter_grade(90), "A")
        self.assertEqual(grade_stats.letter_grade(89.9), "B")
        self.assertEqual(grade_stats.letter_grade(70), "C")
        self.assertEqual(grade_stats.letter_grade(60), "D")
        self.assertEqual(grade_stats.letter_grade(59.9), "F")

    def test_class_summary(self):
        summary = grade_stats.class_summary(self.students)
        self.assertEqual(summary["num_students"], 10)
        self.assertEqual(summary["average"], 77.98)
        self.assertEqual(summary["highest"], 97.2)
        self.assertEqual(summary["lowest"], 54.5)
        self.assertEqual(sum(summary["grade_counts"].values()), 10)

    def test_class_summary_empty(self):
        with self.assertRaises(ValueError):
            grade_stats.class_summary([])


if __name__ == '__main__':
    unittest.main()
