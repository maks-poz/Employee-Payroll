class Employee:     # Creating the Super class
    def __init__(self, name, department):   # Initializing an object with data fields
        self.__name = name                  # that contain employee's name
        self.__department = department      # and department

    def get_name(self):     # Creating a method that returns employee's name
        return self.__name

    def set_name(self, x):  # Creating a method that sets employee's name
        self.__name = x

    def get_department(self):   # Creating a method that returns employee's department
        return self.__department

    def set_department(self, x):    # Creating a method that sets employee's department
        self.__department = x

    def pay(self):      # Pay method that returns a zero float
        x = 0.0
        return x

    def __str__(self):      # str method that returns a summary about an Employee object
        x = f"Name: {self.__name} \nDepartment: {self.__department}"
        return x


class CommissionPaid(Employee):                             # Creating a subclass
    def __init__(self, name, department, base_pay, sales):  # for commission paid employees
        super().__init__(name, department)                  # that inherits name and department
        self.__base_pay = base_pay                          # and additionally has base pay
        self.__sales = sales                                # and sales

    def get_base_pay(self):     # A method that returns employee's base pay
        return self.__base_pay

    def set_base_pay(self, arg):    # A method that sets employee's base pay
        self.__base_pay = arg

    def get_sales(self):    # A method that returns employee's sales
        return self.__sales

    def set_sales(self, arg):   # A method that sets employee's sales
        self.__sales = arg

    def pay(self):      # A method that calculates total pay for employee depending on their sales
        if self.__sales > 8000:
            return (self.__sales * 3)/100 + self.__base_pay
        elif 3000 <= self.__sales <= 8000:
            return (self.__sales * 1.5)/100 + self.__base_pay
        elif self.__sales < 3000:
            return self.__base_pay

    def __str__(self):      # str method that returns a summary about a CommissionPaid object
        x = f"Base pay: {self.__base_pay} \nSales: {self.__sales}"
        return x


class HourlyPaid(Employee):                                             # Creating a subclass
    def __init__(self, name, department, hourly_rate, hours_worked):    # for Hourly Paid employees
        super().__init__(name, department)                              # that inherits name and department
        self.__hourly_rate = hourly_rate                                # and additionally has hourly rate
        self.__hours_worked = hours_worked                              # and number of hours worked

    def get_hourly_rate(self):      # A method that returns hourly rate
        return self.__hourly_rate

    def set_hourly_rate(self, arg):     # A method that sets hourly rate
        self.__hourly_rate = arg

    def get_hours_worked(self):     # A method that returns hours worked
        return self.__hours_worked

    def set_hours_worked(self, arg):    # A method that sets hours worked
        self.__hours_worked = arg

    def pay(self):      # A method that calculates total pay for employee depending on the hours worked
        if self.__hours_worked > 40:
            overtime_pay = self.__hourly_rate * (self.__hours_worked - 40) * 1.75
            regular_pay = self.__hourly_rate * 40
            return overtime_pay + regular_pay
        else:
            return self.__hourly_rate * self.__hours_worked

    def __str__(self):      # str method that returns a summary about a HourlyPaid object
        x = f"Hourly rate: {self.__hourly_rate} \nHours worked: {self.__hours_worked}"
        return x

