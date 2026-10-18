# MLOps Lab 1: GitHub Actions with Pytest and Unittest

![Pytest](https://github.com/bpaduru/mlops-github-actions-lab/actions/workflows/pytest_action.yml/badge.svg)
![Unittest](https://github.com/bpaduru/mlops-github-actions-lab/actions/workflows/unittest_action.yml/badge.svg)

This is my version of Lab 1 from the [MLOps course repo](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1). The lab is about automated testing and CI. It has a small calculator module, tests written with pytest and unittest, and GitHub Actions workflows that run the tests every time code is pushed. I kept the original setup and added my own changes on top of it, which are listed in the "What I changed" section below.

## What you need to install

You only need two things: **Python** and **Git**.

| Tool | Version | Download |
|---|---|---|
| Python | 3.10, 3.11 or 3.12 (these are the versions tested in GitHub Actions) | https://www.python.org/downloads/ |
| Git | any recent version | https://git-scm.com/downloads |

The only Python package used is **pytest 8.3.3**, which gets installed from `requirements.txt` in the setup steps. Everything else (csv, os, unittest) comes with Python.

**Installing Python on Windows:** run the installer and make sure to check the box that says **"Add python.exe to PATH"** on the first screen. If you skip this, the `python` command won't work in the terminal.

**Installing on Mac:** the python.org installer works. On Mac, use `python3` instead of `python` in all the commands below.

To check both are installed, open a terminal (Command Prompt or PowerShell on Windows, Terminal on Mac) and run:

```
python --version
git --version
```

You should see something like `Python 3.11.9` and `git version 2.45.1`. The exact numbers don't need to match as long as Python is 3.10 or higher.

## Setup

### 1. Clone the repo

```
git clone https://github.com/bpaduru/mlops-github-actions-lab.git
cd mlops-github-actions-lab
```

### 2. Create a virtual environment

```
python -m venv lab_env
```

### 3. Activate it

Windows (Command Prompt or PowerShell):
```
lab_env\Scripts\activate
```

Mac or Linux:
```
source lab_env/bin/activate
```

After activating, you should see `(lab_env)` at the start of the terminal line.

If PowerShell gives an error saying running scripts is disabled, run this once and then try activating again:
```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

## How to run it

All commands should be run from the main `mlops-github-actions-lab` folder with the virtual environment activated.

### Run the pytest tests

```
pytest -v
```

A successful run ends with:

```
============================= 40 passed in 0.12s ==============================
```

(The time will be a bit different on your machine.) There are 40 because parametrized tests count each set of inputs as its own test.

### Run the unittest tests

```
python -m unittest test.test_unittest -v
```

A successful run ends with:

```
----------------------------------------------------------------------
Ran 18 tests in 0.005s

OK
```

### Run the grade report

```
python -m src.grade_stats
```

Note: it has to be run with `-m src.grade_stats` like above. Running `python src/grade_stats.py` directly will give an import error because of how Python finds the `src` package.

A successful run prints:

```
Student Grade Report
====================
Alex         92.0   A
Priya        80.0   B
Jordan       63.7   D
Maria        87.7   B
Chen         59.3   F
Sam          97.2   A
Fatima       72.0   C
Lucas        84.1   B
Aisha        54.5   F
Daniel       89.3   B

Class Summary
=============
Students: 10
Average: 77.98
Highest: 97.2
Lowest: 54.5
Grade counts: {'A': 2, 'B': 4, 'C': 1, 'D': 1, 'F': 2}
```

### Check GitHub Actions

The workflows run automatically on GitHub when code is pushed to main or a pull request is opened. To see them, go to the **Actions** tab of this repo. A successful run shows a green checkmark next to both **Testing with Pytest** and **Python Unittests**. The pytest workflow runs 3 jobs (Python 3.10, 3.11 and 3.12), and the test report for each one can be downloaded from the bottom of the run page under Artifacts.

You can also start a run manually: Actions tab → pick a workflow on the left → **Run workflow**.

## What I changed

### 1. Calculator updates (src/calculator.py)
- Added input checks to fun4 since it was the only function without them
- Added fun5 for division, which raises a ZeroDivisionError when dividing by zero
- Added fun6 for powers
- Added fun7 to find the average of a list of numbers, which raises a ValueError for an empty list or non number items

### 2. New dataset and grade stats module
- Added `data/student_scores.csv` with homework, midterm and final scores for 10 students
- Added `src/grade_stats.py` which reads the csv, calculates a weighted score for each student (homework 30%, midterm 30%, final 40%), gives a letter grade (A 90+, B 80+, C 70+, D 60+, F below 60), and prints a class summary
- It checks that scores are numbers between 0 and 100 and gives a clear error if the csv file is missing
- It uses the calculator functions (fun3, fun4, fun7) to do the math, so the two parts of the project are connected

### 3. More tests
- Kept all the original tests
- Added tests for the new calculator functions, including error cases like dividing by zero and passing strings
- Added tests for the grade stats module covering loading the data, a missing file, weighted scores, letter grade boundaries (like 89.9 being a B) and the class summary
- Used `pytest.mark.parametrize` to run the same test with different inputs, and `tmp_path` to test loading a temporary csv file
- In the unittest file I added a second test class for grade stats and used `subTest` so it shows which function failed
- Pytest went from 4 to 40 test cases and unittest went from 4 to 18 tests

### 4. Fixed and updated the workflows (.github/workflows)
The original pytest workflow did not work as is, so I fixed it:
- Fixed the `run-nam` typo to `run-name`
- Removed `branches-ignore` because GitHub does not allow it together with `branches`
- Removed the label and issues triggers since they are not related to testing
- Updated checkout to v4, setup-python to v5 and upload-artifact to v4 (v2 of upload-artifact is no longer supported and fails)
- Python 3.8 is not available on the current ubuntu runner, so I replaced it with a matrix that tests on Python 3.10, 3.11 and 3.12
- Gave each artifact a name with the Python version so the 3 jobs don't overwrite each other
- Added `pull_request` and `workflow_dispatch` triggers so tests also run on pull requests and can be started manually
- Added a step that runs the grade report on the student data
- Pinned pytest to 8.3.3 in requirements.txt so the results are the same on every machine

## Project structure

```
mlops-github-actions-lab/
    .github/workflows/
        pytest_action.yml      runs pytest on Python 3.10, 3.11, 3.12
        unittest_action.yml    runs unittest on Python 3.11
    data/
        student_scores.csv     scores for 10 students
    src/
        calculator.py          math functions
        grade_stats.py         reads the csv and calculates grades
    test/
        test_pytest.py         pytest tests
        test_unittest.py       unittest tests
    requirements.txt
    README.md
```

## Troubleshooting

- **`python` is not recognized:** Python wasn't added to PATH. Reinstall it and check "Add python.exe to PATH", or on Mac use `python3`.
- **`No module named pytest`:** the virtual environment isn't activated or dependencies weren't installed. Activate it and run `pip install -r requirements.txt`.
- **`ModuleNotFoundError: No module named 'src'`:** make sure you're in the main project folder and use `python -m src.grade_stats`, not `python src/grade_stats.py`.
