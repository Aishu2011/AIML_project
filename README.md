# AI/ML Sprint 1 – Python, OOPs and SQL Competency Assessment

## Project Overview

This project is developed as part of the AI/ML Engineer Sprint 1 Assessment. The objective of the project is to demonstrate Python programming, Object-Oriented Programming (OOP), SQL concepts, logging, exception handling, and modular code design.

The application can load data from different file formats, write data into multiple formats, connect to a SQLite database, and execute SQL scripts.

## Project Structure

AIML_project/
│
├── src/
│   ├── __init__.py
│   ├── base_handler.py
│   ├── config.py
│   ├── database.py
│   ├── exceptions.py
│   ├── loader.py
│   ├── logger.py
│   ├── utils.py
│   └── writer.py
│
├── sql/
│   ├── schemas.sql
│   ├── sample_data.sql
│   ├── queries.sql
│   ├── views.sql
│   └── indexes.sql
│
├── data/
│   └── sample.csv
│
├── logs/
├── outputs/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md

## Features

* Load data from CSV, JSON and TXT files.
* Save data as CSV, JSON, TXT and Pickle files.
* Application logging.
* Custom exception handling.
* SQLite database connection.
* Execute SQL scripts.
* Utility functions for validation and execution time.

## OOP Concepts Used

* Classes and Objects
* Inheritance
* Encapsulation
* Composition
* Static Methods
* Class Methods
* Properties
* Type Hinting
* Custom Exceptions

## SQL Concepts Used

* Primary Keys
* Foreign Keys
* Table Relationships
* SELECT
* WHERE
* GROUP BY
* ORDER BY
* INNER JOIN
* LEFT JOIN
* UNION
* CASE Statement
* Subqueries
* Common Table Expressions (CTE)
* Window Functions
* Views
* Indexes

## Requirements

Install the required package:

pip install -r requirements.txt

## How to Run

Run the project using:

python main.py

## Output

After running the project:

* Output files are created inside the **outputs** folder.
* Log messages are stored in **logs/application.log**.
* SQLite database is created as **database.db**.

## Assumptions

* Sample input data is available in the **data** folder.
* SQL scripts are available in the **sql** folder.
* Python and required packages are installed before running the project.

## Future Enhancements

* Support additional file formats such as Excel.
* Improve configuration using environment variables.
* Add more automated test cases.
* Extend database operations with CRUD functionality.
