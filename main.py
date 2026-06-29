from operations import EmployeeManager


def print_menu():
    print("\n" + "=" * 40)
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. List Employees")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    print("\n " + "=" * 40)


def get_input(prompt, required=False):
    """Get user input"""
    while True:
        value = input(prompt).strip()
        if not value and required:
            print("This field is required. Please enter a value.")
            continue
        return value


def main():
    manager = EmployeeManager("employee.csv")

    while True:
        print_menu()
        choice = input("Enter your choice(1-6)").strip()
        # Choice 1 [List Employees] block
        if choice == "1":
            manager.list_employees()

        # Choice 2 [Search Employee] block
        elif choice == "2":
            employee_id = get_input("Enter the EmployeeID:", True)
            emp = manager.search_employee(employee_id)
            if emp:
                print(emp)

        # Choise 3 [Add Employee] block
        elif choice == "3":
            print("-----Add new Employee-----")
            employee_id = get_input("Enter the EmployeeID:", True)
            name = get_input("Enter the name:", True)
            department = get_input("Enter the department:", True)
            email = get_input("Enter the email:", True)
            salary = get_input("Enter the salary:", True)
            manager.add_employee(
                employee_id=employee_id,
                name=name,
                department=department,
                email=email,
                salary=salary,
            )

        # Choice 4 [Update Employee] block
        elif choice == "4":
            print("-----Update Employee-----")
            employee_id = get_input("Enter the employee ID:", True)
            employee = manager.search_employee(employee_id)
            if not employee:
                continue
            print(f"Current data: {employee}")
            print("Leave the specific fields blank to keep the current data.")
            name = input(f"Name [{employee['name']}]: ") or None
            department = input(f"Department [{employee['department']}]: ") or None
            email = input(f"Email [{employee['email']}]: ") or None
            salary = input(f"Salary [{employee['salary']}]: ") or None
            manager.update_employee(employee_id, name, department, email, salary)

        # Choice 5 [Delete Employee] block
        elif choice == "5":
            print("-----Delete Employee-----")
            employee_id = get_input("Enter the employee_id: ", True)
            manager.delete_employee(employee_id)

        # Choice 6 [Exit] block
        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter from 1-6")


if __name__ == "__main__":
    main()
