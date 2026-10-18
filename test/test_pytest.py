import pytest
from src import calculator
from src import grade_stats


# tests from the original lab

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1


def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98


# new calculator tests

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-8, 2, -4),
    (7, 2, 3.5),
    (0, 5, 0),
])
def test_fun5(x, y, expected):
    assert calculator.fun5(x, y) == expected


def test_fun5_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.fun5(10, 0)


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (-2, 2, 4),
    (9, 0.5, 3),
])
def test_fun6(x, y, expected):
    assert calculator.fun6(x, y) == expected


def test_fun7():
    assert calculator.fun7([1, 2, 3]) == 2
    assert calculator.fun7([10]) == 10
    assert calculator.fun7([-5, 5]) == 0
    assert calculator.fun7([1.5, 2.5]) == 2


def test_fun7_empty_list():
    with pytest.raises(ValueError):
        calculator.fun7([])


def test_fun7_bad_items():
    with pytest.raises(ValueError):
        calculator.fun7([1, "two", 3])


# every function should raise ValueError when given a string
@pytest.mark.parametrize("func", [
    calculator.fun1,
    calculator.fun2,
    calculator.fun3,
    calculator.fun5,
    calculator.fun6,
])
def test_two_input_functions_reject_strings(func):
    with pytest.raises(ValueError):
        func("a", 2)


def test_fun4_rejects_strings():
    with pytest.raises(ValueError):
        calculator.fun4(1, 2, "3")


# grade_stats tests

def test_weighted_score():
    assert grade_stats.weighted_score(100, 100, 100) == 100
    assert grade_stats.weighted_score(0, 0, 0) == 0
    assert grade_stats.weighted_score(80, 70, 90) == 81
    assert grade_stats.weighted_score(92, 88, 95) == 92


@pytest.mark.parametrize("homework, midterm, final", [
    (101, 80, 80),
    (80, -5, 80),
    (80, 80, "90"),
])
def test_weighted_score_bad_input(homework, midterm, final):
    with pytest.raises(ValueError):
        grade_stats.weighted_score(homework, midterm, final)


@pytest.mark.parametrize("score, expected", [
    (95, "A"),
    (90, "A"),
    (89.9, "B"),
    (80, "B"),
    (75, "C"),
    (60, "D"),
    (59.9, "F"),
    (0, "F"),
])
def test_letter_grade(score, expected):
    assert grade_stats.letter_grade(score) == expected


def test_load_scores_from_data_folder():
    students = grade_stats.load_scores()
    assert len(students) == 10
    assert students[0]["name"] == "Alex"
    assert students[0]["final"] == 95


def test_load_scores_missing_file():
    with pytest.raises(FileNotFoundError):
        grade_stats.load_scores("not_a_real_file.csv")


def test_load_scores_custom_file(tmp_path):
    # make a small csv just for this test
    test_file = tmp_path / "small.csv"
    test_file.write_text("name,homework,midterm,final\nTom,50,60,70\n")
    students = grade_stats.load_scores(str(test_file))
    assert len(students) == 1
    assert students[0]["name"] == "Tom"
    assert students[0]["homework"] == 50


def test_class_summary():
    students = grade_stats.load_scores()
    summary = grade_stats.class_summary(students)
    assert summary["num_students"] == 10
    assert summary["average"] == 77.98
    assert summary["highest"] == 97.2
    assert summary["lowest"] == 54.5
    assert summary["grade_counts"] == {"A": 2, "B": 4, "C": 1, "D": 1, "F": 2}


def test_class_summary_empty():
    with pytest.raises(ValueError):
        grade_stats.class_summary([])
