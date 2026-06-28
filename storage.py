import csv
import os
from employee import Employee


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load_employees(self):
        # Create a list to store the Employee objects
        emp_objects = list()
        # Check if the file exists or there's any data in it to prevent errors
        if os.path.exists(self.filename) or not os.path.getsize(self.filesize) == 0:
            # Open the file in read mode
            with open(self.filename, mode="r", newline="") as file:
                # Use the csv.DictReader() method to import all entries as a list of dictionaries
                emp_data = csv.DictReader(file)
                for i in emp_data:
                    # Iterate through the list and create Employee objects of each entries
                    emp = Employee(
                        employee_id=i["employee_id"],
                        name=i["name"],
                        department=i["department"],
                        email=i["email"],
                        salary=i["salary"],
                    )
                    # Assign the employee objects to emp_objects to return
                    emp_objects.append(emp)
        return emp_objects

    def save_employees(self, employees):
        # Define the fieldnames to be used in the DistWriter method
        fieldnames = ["employee_id", "name", "department", "email", "salary"]

        # Open the file on append mode
        with open(self.filename, mode="w", newline="") as file:
            # Create a DistWriter object
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write the header row first
            writer.writeheader()
            # Go through the list of employee objects, convert the objects into a dictionary, and write to the file
            for employee in employees:
                emp = {
                    "employee_id": employee.employee_id,
                    "name": employee.name,
                    "department": employee.department,
                    "email": employee.email,
                    "salary": employee.salary,
                }
                writer.writerow(emp)
                # Note: full rewrite on every save is intentional for simplicity.
                # For large datasets, consider append-only writes with indexed lookups.
