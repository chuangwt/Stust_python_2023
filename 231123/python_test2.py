class Employee:

    def __init__(self, i, n, s, d):
        self.emp_id = i
        self.emp_name = n
        self.emp_salary = s
        self.emp_department = d

    def calculate_emp_salary(self, hours):
        time = 0
        if hours > 50:
            time = hours - 50
        self.emp_salary = self.emp_salary + (time * (self.emp_salary / 50))


    def emp_assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print ("name:", self.emp_name)
        print ("ID:", self.emp_id)
        print ("salary:", self.emp_salary)
        print ("department:", self.emp_department)
        print ("\n")


emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")


print("Original Employee Details:")
emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()


emp1.emp_assign_department("OPERATIONS")
emp4.emp_assign_department("SALES")


emp2.calculate_emp_salary(70)
emp4.calculate_emp_salary(58)


print("Updated Employee Details:")
emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()
