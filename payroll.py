from employees import Employee, CommissionPaid, HourlyPaid  # importing classes from employees.py

g_count = 0     # Global variable for the count of employees


def main():  # main function
    global g_count  # initializing the global variable
    employee_objects = []   # creating a list of employees
    active = True   # creating the condition for the loop below

    while active:
        subclass = input("Enter employee's subclass (Commission/Hourly): ")     # Getting the
        name = input("Enter employee's name: ")                                 # info from
        department = input("Enter employee's department: ")                     # the user
        rate = int(input("Enter employee's base pay/hourly rate: "))
        coefficient = int(input("Enter employee's total sales/hours worked: "))

        if subclass == "Commission":                                            # Matching with
            employee = CommissionPaid(name, department, rate, coefficient)      # the subclass
            employee_objects.append(employee)                                   # Adding to the list
            g_count += 1                                                        # Updating the employee counter
            check = input("Do you want to add more employees? (Y/N): ")

            if check.lower() == "n":    # Checking the loop condition
                active = False

        elif subclass == "Hourly":                                      # Matching with
            employee = HourlyPaid(name, department, rate, coefficient)  # another subclass
            employee_objects.append(employee)                           # Adding to the list
            g_count += 1                                                # Updating the employee counter
            check = input("Do you want to add more employees? (Y/N): ")

            if check.lower() == "n":    # Checking the loop condition
                active = False

    print_employee_list(employee_objects)                                   # Printing a table of employees
    print(f"\nTotal pay for the week: ${total_pay(employee_objects)}")      # Printing to total payout


def total_pay(lst):  # total pay function that
    total = 0.0  # calculates total pay
    for i in lst:  # for all the employees
        total += i.pay()
    return total


def print_employee_list(lst):  # Function that prints final output
    global g_count
    print(f"{'Employee Name':<20}{'Department':<20}{'Weekly Pay':<20}")
    print("-" * 52)
    for i in range(g_count):    # Loop for printing rows with employees' data
        print(f"{lst[i].get_name():<20}{lst[i].get_department():<20}{lst[i].pay()}")


main()  # main function called
