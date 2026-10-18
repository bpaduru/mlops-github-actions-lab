# MLOps Lab 1: GitHub Actions with Pytest and Unittest

![Pytest](https://github.com/bpaduru/mlops-github-actions-lab/actions/workflows/pytest_action.yml/badge.svg)
![Unittest](https://github.com/bpaduru/mlops-github-actions-lab/actions/workflows/unittest_action.yml/badge.svg)

This is my version of Lab 1 from the [MLOps course repo](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1). The original lab has a small calculator module, tests written with pytest and unittest, and GitHub Actions workflows that run the tests on every push. I kept the original setup and added my own changes on top of it.

## What I changed

### 1. Calculator updates (src/calculator.py)
- Added input checks to fun4 since it was the only function without them
- Added fun5 for division, which raises an error when dividing by zero
- Added fun6 for powers
- Added fun7 to find the average of a list of numbers

### 2. New dataset and grade stats module
- Added `data/student_scores.csv` with homework, midterm and final scores for 10 students
- Added `src/grade_stats.py` which reads the csv, calculates a weighted score for each student (homework 30%, midterm 30%, final 40%), gives a letter grade, and prints a class summary
- The grade stats module uses the calculator functions (fun3, fun4, fun7) to do the math so the two parts of the project are connected

### 3. More tests
- Kept all the original tests
- Added tests for the new calculator functions, including error cases like dividing by zero and passing strings
- Added tests for the grade stats module, including loading the data, weighted scores, letter grade boundaries and the class summary
- Used `pytest.mark.parametrize` to run the same test with different inputs and `tmp_path` to test loading a custom csv file
- Pytest now runs 40 test cases and unittest runs 18 tests

### 4. Fixed and updated the workflows
The original pytest workflow did not work as is, so I fixed it:
- Fixed the `run-nam` typo to `run-name`
- Removed `branches-ignore` because GitHub does not allow it together with `branches`
- Removed the label and issues triggers since they are not related to testing
- Updated checkout to v4, setup-python to v5 and upload-artifact to v4 (v2 is no longer supported)
- Python 3.8 is not available on the current ubuntu runner, so I replaced it with a matrix that tests on Python 3.10, 3.11 and 3.12
- Added `pull_request` and `workflow_dispatch` triggers so tests also run on pull requests and can be started manually
- Added a step that runs the grade report on the student data

## Project structure

```
mlops-github-actions-lab/
    .github/workflows/
        pytest_action.yml
        unittest_action.yml
    data/
        student_scores.csv
    src/
        calculator.py
        grade_stats.py
    test/
        test_pytest.py
        test_unittest.py
    requirements.txt
    README.md
```

## How to run it

Clone the repo and set up a virtual environment:

```
git clone https://github.com/bpaduru/mlops-github-actions-lab.git
cd mlops-github-actions-lab
python -m venv lab_env
lab_env\Scripts\activate
pip install -r requirements.txt
```

On Mac or Linux use `source lab_env/bin/activate` instead.

Run the tests:

```
pytest -v
python -m unittest test.test_unittest -v
```

Run the grade report:

```
python -m src.grade_stats
```

## Sample output

```
Class Summary
=============
Students: 10
Average: 77.98
Highest: 97.2
Lowest: 54.5
Grade counts: {'A': 2, 'B': 4, 'C': 1, 'D': 1, 'F': 2}
```

## GitHub Actions

Both workflows run automatically when I push to main or open a pull request. The results can be seen in the Actions tab of this repo. The pytest workflow also saves the test report as an artifact for each Python version.
