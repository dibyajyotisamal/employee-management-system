from storage import Storage
from employee import Employee
from email_validator import validate_email


class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
        self.storage = Storage(self.filename)
        self.employees = self.storage.load_employees()

    def list_employees(self):
        """Return list of all employees."""
        if len(self.employees):
            for employee in self.employees:
                print(employee)
        else:
            print("No employees found.")

    def add_employee(self, employee_id, name, department, email, salary):
        """Add a new employee."""
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

    def search_employee(self, employee_id):
        """Find employee by ID. Returns Employee or None."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def delete_employee(self, employee_id):
        """Delete employee by ID."""
        employee = self.search_employee(employee_id)
        if employee:
            self.employees.remove(employee)
            self.storage.save_employees(self.employees)
            print("Successfully removed the employee info.")
        else:
            print(f"Employee with ID {employee_id} not found. Can't delete.")

    def update_employee(
        self, employee_id, name=None, department=None, email=None, salary=None
    ):
        """Update employee attributes by ID"""
        emp = self.search_employee(employee_id)
        # If the search_employee method does not return an Employee object print and exit
        if not emp:
            print("Employee not found.")
            return None
        # -------VALIDATE ALL INPUTS--------------
        # If email is provided, check if its valid first, then update the object
        if email:
            # Check if the provided email is valid
            try:
                validate_email(email, check_deliverability=False)
            except Exception as e:
                print(f"Email is invalid. {str(e)}")
                return
        # If salary is provided validate it first then update the object
        if salary:
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

        # ---------------APPLY CHANGES AFTER VALIDATION------------
        # If name is provided, update the object name
        if name:
            emp.name = name
        # If department is provided, update the object department
        if department:
            emp.department = department
        # If email is provided, update the object email
        if email:
            emp.email = email
        # If salary is provided, update the object salary
        if salary:
            emp.salary = salary

        # SAVE THE UPDATED EMPLOYEES LIST
        self.storage.save_employees(self.employees)
        print("Employee data updated successfully.")
        return True
