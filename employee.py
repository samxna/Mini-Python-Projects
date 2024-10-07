# Samina Ahmed | 220023354 | 04/2023
# IN0007 Lab 2 Assessment | Q2

# Creating a class Employee with the following attributes.
class Employee:
    emp_id = ""
    emp_name = ""
    emp_salary = 0
    emp_department = ""

    # To calculate employers salary, given their salary + hours worked. 
    def calculate_emp_salary(self, salary, hours_worked):
        # Only if they work more than 50 hours, it will follow this if statement. 
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (salary / 50))
            self.emp_salary = salary + overtime_amount
        else:
            self.emp_salary = salary

    # To change the departments of employees. 
    def emp_assign_department(self, department):
        self.emp_department = department

    # Output all the final information regarding an employee
    def print_employee_details(self):
        print("Name:", self.emp_name)
        print("ID:", self.emp_id)
        print("Salary:", int(self.emp_salary))
        print("Department:", self.emp_department)
        print("\n")

# Create an instance of Employee
emp = Employee()

# Assign values to attributes
emp.emp_id = "220023354"
emp.emp_name = "SAMINA AHMED"
emp.calculate_emp_salary(6000, 55)
emp.emp_assign_department("CYBER SECURITY")

# Print employee details
emp.print_employee_details()

