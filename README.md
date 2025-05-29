# CSV-data-analysis
Python Programming Assignment 1
Title: Foundations of Python Programming and CSV Data Analysis
Objective:
To build strong foundations in Python programming and introduce file handling with real-world data formats (CSV), enabling students to design simple yet functional data-driven applications.

Learning Outcomes
By the end of this assignment cycle, students will be able to:
Write clean, modular Python scripts using core programming constructs


Understand data types, loops, conditionals, and functions in Python


Read, process, and write data from/to .txt and .csv files


Apply basic analysis techniques on structured tabular data


Develop interactive, console-based applications with persistent data



Topics Covered
Python environment setup (VS Code)


Variables, expressions, and data types: int, float, str, bool


Input/output: input(), print()


Operators: arithmetic, comparison, logical


Conditional statements: if, else, elif


Loops: for, while, range()


Functions: defining and invoking


Basic data structures: list, dict


Exception handling: try-except


Writing modular and reusable code


File operations: open(), read(), write(), with statement


Reading .txt files line-by-line


Introduction to the csv module: csv.reader, csv.writer


Manipulating structured data using lists and dictionaries


Performing simple aggregations: totals, averages, min, max


Writing and appending structured CSV records


Optional: Introduction to pandas for high-level data analysis



Assignment Tasks
Task: Text File Analyzer
Read a .txt file


Count and display:


Total number of lines


Total number of words


Total number of characters


Task: CSV Reader – Student Scores
Read students.csv with format:
Name,Math,Science,English
Ayaan,78,84,69
Reema,91,89,75
Dev,66,70,58


For each student:


Calculate total and average marks


Identify and display the top scorer


Handle malformed or missing data gracefully


Task: CSV Writer – Add New Student
Accept student name and three subject marks from user input


Append the data as a new row to students.csv


Confirm that the data was written successfully



Mini Project: Student Report Card Manager (Console-Based)
Goal: Build a functional Python application that supports both analysis and entry of student records using CSV as backend storage.
Functional Requirements:
Load and display all student records in a formatted table


Add a new record through user input and append it to the CSV


Calculate and display the student with the highest total score


Validate input values (e.g., marks between 0 and 100)


Optional: Implement a search by student name


Sample
=== Student Report Card Menu ===
1. View All Records
2. Add New Record
3. Show Topper
4. Exit
Enter your choice:

