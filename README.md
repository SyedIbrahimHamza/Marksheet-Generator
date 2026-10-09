# Student Marksheet Generator

A simple terminal-based Student Marksheet Generator built with Python.

This program allows users to enter a student's name and marks in five subjects, calculate the total marks and percentage, assign a grade, and determine whether the student has passed or failed.

## Features

* Enter student name
* Input marks for five subjects
* Validate marks between 0 and 100
* Handle invalid input using exception handling
* Calculate total marks
* Calculate percentage
* Assign grades based on percentage
* Determine pass or fail status
* Display a complete student marksheet
* Store student results using a list and dictionary

## Subjects

The program calculates results for the following five subjects:

| Subject | Maximum Marks |
|---|---:|
| Mathematics | 100 |
| Physics | 100 |
| Chemistry | 100 |
| English | 100 |
| Computer | 100 |
| **Total** | **500** |

## Grading System

The program assigns grades according to the student's percentage.

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 80% – 89.99% | A |
| 70% – 79.99% | B |
| 60% – 69.99% | C |
| 50% – 59.99% | D |
| Below 50% | F |

### Passing Criteria

* **PASS:** Percentage is 50% or above.
* **FAIL:** Percentage is below 50%.

## How the Program Works

1. An empty `marksheet` list is created to store student results.
2. The program asks the user to enter the student's name.
3. The program displays prompts for marks in five subjects.
4. Each subject's marks must be a whole number between 0 and 100.
5. If the user enters invalid input, the program displays an error message and asks again.
6. The `calculate_result()` function calculates total marks and percentage.
7. The program assigns a grade based on the percentage.
8. The program determines whether the student has passed or failed.
9. Student information and calculated results are stored in a dictionary.
10. The dictionary is added to the `marksheet` list.
11. The program displays the student's complete marksheet.

## Example

Suppose a student enters the following marks:

| Subject | Marks |
|---|---:|
| Mathematics | 90 |
| Physics | 85 |
| Chemistry | 80 |
| English | 75 |
| Computer | 95 |
| **Total** | **425 / 500** |

Percentage calculation:

```text
Percentage = (Total Marks / Maximum Marks) × 100
Percentage = (425 / 500) × 100
Percentage = 85%
```

The student's grade is **A**, and the status is **PASS**.

## Example Program Output

```text
Enter student name: Ali
Enter Math marks (0-100): 90
Enter Physics marks (0-100): 85
Enter Chemistry marks (0-100): 80
Enter English marks (0-100): 75
Enter Computer marks (0-100): 95

===== MARKSHEET =====
Name: Ali
Marks: [90, 85, 80, 75, 95]
Total: 425 / 500
Percentage: 85.0 %
Grade: A
Status: PASS
=====================
```

## Input Validation

The program uses `while True`, `try-except`, and conditional statements to validate marks.

### 1. Marks Range Validation

Marks must be between 0 and 100.

Example:

```text
Enter Math marks (0-100): 120
Marks must be between 0 and 100.
```

### 2. Invalid Input Handling

If the user enters text instead of a whole number, the program displays an error message.

Example:

```text
Enter Math marks (0-100): abc
Please enter a valid whole number.
```

The program asks for the marks again until valid input is provided.

## Function

### `calculate_result(name, marks)`

This function:

* Calculates the total marks using `sum()`.
* Calculates the percentage.
* Assigns a grade using `if`, `elif`, and `else`.
* Determines the pass or fail status.
* Creates a dictionary containing student information and results.
* Stores the dictionary in the `marksheet` list.

## Data Storage

The program uses a list to store student results.

```python
marksheet = []
```

Each student's information is stored in a dictionary:

```python
student = {
    "name": name,
    "marks": marks,
    "total": total,
    "percentage": percentage,
    "grade": grade,
    "status": status
}
```

The dictionary is added to the list:

```python
marksheet.append(student)
```

The program then uses a `for` loop to display the stored results.

## Python Concepts Used

This project practices the following Python concepts:

* Variables
* Functions
* Lists
* Dictionaries
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `try-except` exception handling
* `input()`
* `int()`
* `sum()`
* `round()`
* `.append()`
* Dictionary keys and values
* Arithmetic operations
* Comparison operators
* Function arguments
* User input validation
* Percentage calculations
* Conditional grading logic

## Project Structure

```text
student-marksheet/
│
├── Student_Marksheet_Generator.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the installed version:

```bash
python --version
```

### 2. Save the Program

Save your Python code as:

```text
Student_Marksheet_Generator.py
```

### 3. Run the Program

Open a terminal in the project directory and execute:

```bash
python Student_Marksheet_Generator.py
```

## Purpose

This project is created for Python practice and learning.

It helps beginners understand how functions, lists, dictionaries, loops, conditional statements, exception handling, and input validation can be combined to build a simple student result management program.

## Limitations

* The program processes one student's result per execution.
* Results are stored in memory and are not saved to a file or database.
* Each subject has a maximum of 100 marks.
* The grading and passing criteria are predefined in the code.

## License

This project is intended for educational and practice purposes.
