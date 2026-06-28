class Employee:
    def __init__(self, employee_id, name, department, email, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.email = email
        self.salary = salary

    def __repr__(self):
        return (
            f"Employee(ID: {self.employee_id}, Name: {self.name}, "
            f"Department: {self.department}, Email: {self.email}, "
            f"Salary: {self.salary})"
        )
