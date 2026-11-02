Project Overview

The Data Analyzer and Transformer is a menu-driven Python application developed to analyze and transform one-dimensional (1D) and two-dimensional (2D) list data.

This project allows users to perform different operations such as calculating basic statistics, finding duplicates, filtering values, sorting data, and calculating factorials using recursion.

It demonstrates the practical use of Python built-in functions, user-defined functions, lambda functions, recursion, and different programming concepts.

Features

1. Data Input

Allows users to enter data manually or select sample data.

Supports both 1D and 2D lists.

Converts user input into integer or float values.

Displays the entered dataset.

2. Data Summary Using Built-in Functions

Calculates the total number of elements using len().

Calculates the sum using sum().

Finds minimum and maximum values using min() and max().

Calculates the average of the dataset.

Displays dataset information using **kwargs.

3. Factorial Using Recursion

Accepts a number from the user.

Calculates the factorial using a recursive function.

Displays the factorial result.

Handles negative and invalid inputs.

4. Data Filtering Using Lambda Functions

Allows users to enter a threshold value.

Filters values above or below the given threshold.

Uses lambda() with filter() to select values.

Uses map() to transform filtered values.

5. Sorting Data

Sorts 1D list values in ascending or descending order.

Sorts 2D list rows based on their sum.

Uses the sort() method and sorted() function.

6. Dataset Statistics

Finds the minimum value.

Finds the maximum value.

Calculates the average value.

Returns multiple values from a single function.

7. Find Duplicates and Unique Values

Identifies duplicate values in the dataset.

Displays unique values without repetition.

Uses Python sets for data handling.

8. Global Dataset Summary

Uses the global keyword.

Stores the total number of values and overall average.

Allows different functions to access the dataset summary.

9. Menu-Driven Interface

The program provides nine menu options:

Input Data.

Display Data Summary.

Calculate Factorial.

Filter Data by Threshold.

Sort Data.

Display Dataset Statistics.

Find Duplicates and Unique Values.

Display Global Dataset Summary.

Exit Program.

Programming Concepts Used

Python Programming

Built-in Functions (len(), sum(), min(), max())

User-defined Functions (UDF)

*args and **kwargs

__doc__ attribute

Recursion

Lambda Functions

map() and filter()

Global Keyword

Returning Multiple Values

1D and 2D Lists

Sorting using sort() and sorted()

Loops and Conditional Statements

Type Casting

Input Validation

Technologies Used

Programming Language: Python 3

IDE: VS Code / Python IDLE

Libraries: No external libraries required.

How to Run the Project

Clone or download this repository.

Open the project folder in VS Code or Python IDLE.

Open the terminal.

Run the following command:

python data_analyzer.py

Sample Output

1. Main Menu

WELCOME TO THE DATA ANALYZER AND TRANSFORMER PROGRAM

============== MAIN MENU ==============
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics
7. Find Duplicates and Unique Values
8. Display Global Dataset Summary
9. Exit Program

Please enter your choice:

2. Data Input

Select Data Input:
1. Enter Data Manually
2. Use Sample Data

Enter your choice: 2

Select Data Type:
1. 1D List
2. 2D List

Enter your choice: 1

Data entered successfully!

[10, 20, 30, 40, 50, 20]

3. Data Summary

--- Data Summary ---

Total Values: 6
Sum: 170
Minimum: 10
Maximum: 50
Average: 28.33

4. Factorial Using Recursion

Enter a number: 5

Factorial of 5 is: 120

5. Filter Data Using Lambda

Enter threshold value: 20

1. Values Above Threshold
2. Values Below Threshold

Enter your choice: 1

Filtered Data: [30, 40, 50]

Doubled Filtered Data: [60, 80, 100]

6. Sorting Data

1. Ascending Order
2. Descending Order

Enter your choice: 1

Sorted 1D Data: [10, 20, 20, 30, 40, 50]

7. Find Duplicates and Unique Values

Duplicate Values: [20]

Unique Values: [40, 10, 50, 20, 30]

8. Exit Program

Thank you for using the Data Analyzer and Transformer Program!

Program exited successfully. Goodbye!
