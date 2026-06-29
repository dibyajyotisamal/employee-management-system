# Employee Management System (EMS)

A command-line employee management system built with Python and CSV file storage. Designed as a learning project to practice object-oriented design, file I/O, and clean code architecture.

## Features

- **Add** new employees with validation (unique ID, valid email, positive salary)
- **List** all employees
- **Search** employees by ID
- **Update** employee fields with partial updates (leave blank to keep current value)
- **Delete** employees by ID
- **Persistent storage** using CSV files

## Tech Stack

- Python 3
- `csv` module (built-in)
- `email-validator` for email validation

## Project Structure

employee-management-system/
├── .gitignore
├── README.md
├── requirements.txt
├── employee.py          # Employee data model
├── storage.py           # CSV persistence layer
├── operations.py        # Business logic (EmployeeManager)
└── main.py              # CLI interface

## Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd employee-management-system

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Menu Options

| Option | Action |
|--------|--------|
|1|List Employees|
|2|Search Employee|
|3|Add Employee|
|4|Update Employee|
|5|Delete Employee|
|6|Exit|

## Architecture Highlights

- Data model (employee.py), storage (storage.py), business logic (operations.py), and UI (main.py) are decoupled
- Internal _find_employee() returns live references for mutations; public search_employee() returns read-only dictionaries
- All inputs validated before any state changes

## Future Improvements

- Unit tests with pytest
- Integration tests with Selenium (for future web interface)
- SQLite or database backend
- REST API with Flask/FastAPI
- Web frontend

## License

MIT
