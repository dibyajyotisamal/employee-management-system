import csv
import os
from employee import Employee


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load_employees(self):
        if os.path.exists(self.filename):
            emp_data = csv.DictReader(self.filename)
        else:
            print(f"{self.filename} didn't exist. \n Creating self.filename")
            os.mkdir(self.filename)

        return []

    def save_employees(self, employee):
        pass


s = Storage("employee_data.csv")
