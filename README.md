# Employee Payroll System

## Overview
The Employee Payroll System is a Python-based project designed to calculate the weekly pay for employees based on their job type. The program uses Object-Oriented Programming (OOP) principles, with a superclass `Employee` and two subclasses `CommissionPaid` and `HourlyPaid`. This project demonstrates class inheritance and method overriding, providing a flexible way to calculate pay for different employee types.

## Project Structure
The project is divided into two main files:
1. **employees.py**: 
   - Contains the `Employee` class and two subclasses: `CommissionPaid` and `HourlyPaid`.
   - `Employee`: The superclass that holds general information about the employee (name, department) and provides a base method for calculating pay.
   - `CommissionPaid`: A subclass that calculates the pay for commission-based employees. The pay is calculated as a combination of base pay and commissions, with a bonus if sales exceed a certain threshold.
   - `HourlyPaid`: A subclass that calculates the pay for hourly-based employees based on their hourly wage and hours worked.

2. **payroll.py**:
   - Contains the main logic for handling employee data input and calculating total payroll.
   - Prompts the user to input employee details, including name, department, job type (commission-based or hourly), base pay, and sales or hours worked.
   - Displays a summary of all employees and their respective weekly pay, along with the total payroll for the week.

## Key Features
- **Inheritance**: Demonstrates the use of inheritance to create subclasses (`CommissionPaid`, `HourlyPaid`) from the superclass `Employee`.
- **Method Overriding**: The `pay()` method is overridden in each subclass to calculate pay based on the employee's job type.
- **User Input**: The program prompts the user to enter employee data interactively.
- **Total Payroll Calculation**: Calculates and displays the total payroll for all employees.

## How to Run
1. Clone the repository from GitHub.
2. Run the `payroll.py` file:
3. Follow the prompts to input employee data (name, department, job type, base pay, and sales/hours worked).
4. The program will output a summary of employee pay and the total payroll for the week.

## Requirements
- Python 3.x

## Future Improvements
- Add validation for user input to ensure only valid data is entered.
- Expand the system to handle additional job types (e.g., salaried employees).
- Integrate with a database to persist employee data.

## Author
Maksym Pozomin

