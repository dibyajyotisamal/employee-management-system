from storage import Storage
from employee import Employee
from email_validator import validate_email


class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
        self.storage = Storage(self.filename)
        self.employees = self.storage.load_employees()

    def list_employees(self):
        if len(self.employees):
            for employee in self.employees:
                print(employee)
        else:
            print("No employees found.")

    def add_employee(self, employee_id, name, department, email, salary):
        # Check if the employeeID is already present
        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("Employee information already exists")
                return
        # Check if the provided email is valid
        try:
            validate_email(email, check_deliverability=False)
        except Exception as e:
            print(f"Email is invalid. {str(e)}")
            return
        # Check if the entered salary is number or not
        try:
            salary = float(salary)
        except ValueError:
            print("The salary must be a number")
            return
        # Check if the entered salary is positive or not
        if salary < 0:
            print("Salary is invalid")
            return

        # After all checks are complete, create the Employee object
        emp = Employee(employee_id, name, department, email, salary)

        # Append the new Employee object to the list of Employee objects
        self.employees.append(emp)

        # Call the save_employees method to save the new employee info to the csv file
        self.storage.save_employees(self.employees)
        print("Employee successfully added..!!")
        print(emp)
