import csv
import os
from employee import Employee


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def file_is_empty(self):
        # Check if the file exists or if file is empty before extracting information
        return os.path.exists(self.filename) or os.path.getsize(self.filename) == 0

    def load_employees(self):
        # Create a list to store the Employee objects
        emp_objects = list()
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

    def save_employees(self, employee):
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.DistWriter(file, fieldname=employee.keys())
