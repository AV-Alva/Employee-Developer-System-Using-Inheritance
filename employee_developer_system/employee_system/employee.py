from employee_system.exceptions import (
    InvalidSalaryError,
    MissingInformationError
)

from employee_system.logger_config import logger


class Employee:
    """Parent class representing an employee."""

    def __init__(self, employee_id, name, salary, department):

        if not employee_id or not name or not department:
            logger.error("Employee information is missing.")
            raise MissingInformationError(
                "Employee ID, name and department are required."
            )

        if salary <= 0:
            logger.error(
                f"Invalid salary provided for employee {employee_id}"
            )
            raise InvalidSalaryError(
                "Salary must be greater than zero."
            )

        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

        logger.info(
            f"Employee created successfully: {self.employee_id}"
        )

    def display_details(self):
        """Display employee information."""

        print("\n----- Employee Details -----")
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      : ₹", self.salary)
        print("Department  :", self.department)