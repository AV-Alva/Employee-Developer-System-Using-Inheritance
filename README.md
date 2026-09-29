# Employee & Developer System Using Inheritance

## 📌 Project Overview

This project demonstrates **Object-Oriented Programming (OOP) in Python**, with a primary focus on **inheritance**.

The application contains a parent class called `Employee` and a child class called `Developer`.

The `Developer` class inherits common employee attributes and functionality from the `Employee` class while adding developer-specific information such as programming language and experience.

The project also demonstrates:

- Classes and objects
- Parent and child classes
- Inheritance
- Constructors
- Instance methods
- `super()`
- Packages and modules
- Custom exceptions
- Exception handling
- Logging

---

## 🎯 Objective

The objective of this project is to understand how **inheritance** allows one class to reuse and extend the functionality of another class.

The relationship used in this project is:

```text
Employee
    |
    └── Developer
```

A `Developer` **is an Employee**, so every Developer automatically receives the common Employee attributes and methods.

---

## 📁 Project Structure

```text
employee_developer_system/
│
├── main.py
│
├── employee_system/
│   ├── __init__.py
│   ├── employee.py
│   ├── developer.py
│   ├── exceptions.py
│   └── logger_config.py
│
├── logs/
│   └── employee_system.log
│
└── README.md
```

---

## 🧩 Modules

### `employee.py`

Contains the parent `Employee` class.

The Employee class stores:

- Employee ID
- Name
- Salary
- Department

It also contains:

```python
display_details()
```

This method displays the employee's information.

---

### `developer.py`

Contains the child `Developer` class.

```python
class Developer(Employee):
```

The Developer class inherits from `Employee` and adds:

- Programming language
- Years of experience

It also contains:

```python
display_developer_details()
```

This method displays both the inherited employee information and developer-specific information.

---

### `exceptions.py`

Contains custom exceptions used by the application.

```python
InvalidSalaryError
InvalidExperienceError
MissingInformationError
```

These custom exceptions make error handling easier to understand and maintain.

For example:

```python
if salary <= 0:
    raise InvalidSalaryError(
        "Salary must be greater than zero."
    )
```

---

### `logger_config.py`

Configures Python's `logging` module.

Application activities and errors are stored inside:

```text
logs/employee_system.log
```

Example log entries:

```text
INFO - Employee created successfully: EMP001
INFO - Developer created successfully: DEV001
ERROR - Invalid experience for developer DEV003
```

---

### `main.py`

This is the entry point of the application.

It:

1. Creates Employee and Developer objects.
2. Displays their details.
3. Demonstrates inheritance.
4. Handles custom exceptions.
5. Records application activities using logging.

---

## 🧠 Understanding Inheritance

Inheritance allows a child class to access the properties and methods of its parent class.

The parent class is:

```python
class Employee:
```

The child class is:

```python
class Developer(Employee):
```

This means `Developer` inherits functionality from `Employee`.

For example, `display_details()` is defined inside `Employee`:

```python
def display_details(self):
    print("Employee ID :", self.employee_id)
    print("Name        :", self.name)
    print("Salary      :", self.salary)
    print("Department  :", self.department)
```

However, a Developer object can directly call it:

```python
developer1.display_details()
```

This works because `Developer` inherits from `Employee`.

---

## 🔄 Understanding `super()`

Inside the Developer constructor, the following code is used:

```python
super().__init__(
    employee_id,
    name,
    salary,
    department
)
```

`super()` allows the child class to call functionality from its parent class.

Instead of repeating:

```python
self.employee_id = employee_id
self.name = name
self.salary = salary
self.department = department
```

inside `Developer`, the Employee constructor is reused.

Conceptually:

```text
Developer object created
        |
        v
Developer.__init__()
        |
        v
super().__init__()
        |
        v
Employee.__init__()
        |
        v
Employee attributes initialized
        |
        v
Developer-specific attributes initialized
```

This demonstrates **code reuse**, which is one of the main advantages of inheritance.

---

## 👨‍💻 Objects Created

The program creates at least three objects.

### Employee

```python
employee1 = Employee(
    "EMP001",
    "Arjun",
    50000,
    "Finance"
)
```

### Python Developer

```python
developer1 = Developer(
    "DEV001",
    "Meera",
    75000,
    "Technology",
    "Python",
    5
)
```

### Java Developer

```python
developer2 = Developer(
    "DEV002",
    "Rahul",
    85000,
    "Technology",
    "Java",
    7
)
```

---

## ⚠️ Exception Handling

The application uses `try` and `except` blocks so that errors can be handled gracefully.

Example:

```python
try:
    employee1 = Employee(
        "EMP001",
        "Arjun",
        50000,
        "Finance"
    )

except InvalidSalaryError as error:
    print("Salary Error:", error)
```

---

## 🚫 Invalid Salary Example

If an employee is created with:

```python
employee2 = Employee(
    "EMP002",
    "Ananya",
    -50000,
    "HR"
)
```

the application raises:

```text
InvalidSalaryError
```

with the message:

```text
Salary must be greater than zero.
```

---

## 🚫 Invalid Experience Example

If a developer is created with negative experience:

```python
developer3 = Developer(
    "DEV003",
    "Kiran",
    90000,
    "Technology",
    "C++",
    -3
)
```

the application raises:

```text
InvalidExperienceError
```

with the message:

```text
Experience cannot be negative.
```

---

## 📝 Logging

Logging is used to record successful operations and errors.

Logs are stored in:

```text
logs/employee_system.log
```

The logger records information such as:

```text
Employee created successfully
Developer created successfully
Invalid salary
Invalid experience
Missing employee information
Unexpected application errors
```

Logging is useful in real-world applications because it helps developers understand what happened when a program was running, especially when troubleshooting errors.

---

## ▶️ How to Run the Project

Open the project folder in VS Code.

Make sure the terminal is pointing to:

```text
employee_developer_system/
```

Run:

```bash
python main.py
```

---

## 📤 Sample Output

```text
========== EMPLOYEE ==========

----- Employee Details -----
Employee ID : EMP001
Name        : Arjun
Salary      : ₹ 50000
Department  : Finance


========== DEVELOPER 1 ==========

----- Employee Details -----
Employee ID : DEV001
Name        : Meera
Salary      : ₹ 75000
Department  : Technology
Programming Language : Python
Experience           : 5 years


========== DEVELOPER 2 ==========

----- Employee Details -----
Employee ID : DEV002
Name        : Rahul
Salary      : ₹ 85000
Department  : Technology
Programming Language : Java
Experience           : 7 years
```

---

## 🔑 Key Concepts Learned

| Concept | Implementation |
|---|---|
| Parent Class | `Employee` |
| Child Class | `Developer` |
| Inheritance | `class Developer(Employee)` |
| Constructor | `__init__()` |
| Parent Constructor | `super().__init__()` |
| Object Creation | Employee and Developer objects |
| Instance Method | `display_details()` |
| Package | `employee_system` |
| Modules | Employee, Developer, Exceptions, Logger |
| Custom Exception | `InvalidSalaryError`, etc. |
| Exception Handling | `try / except` |
| Logging | `employee_system.log` |
| Code Reuse | Developer reuses Employee functionality |

---

## 💡 Key Takeaway

**Inheritance allows a child class to reuse and extend the properties and methods of a parent class.**

In this project:

```text
Employee
   |
   └── Developer
```

Every Developer is an Employee, so a Developer automatically receives:

```text
employee_id
name
salary
department
display_details()
```

and extends the Employee class with:

```text
programming_language
experience
display_developer_details()
```

This reduces code duplication and makes applications easier to organize, maintain, and extend.
