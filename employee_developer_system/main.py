from employee_system import Employee, Developer
from employee_system.exceptions import (
    InvalidSalaryError,
    InvalidExperienceError,
    MissingInformationError
)
from employee_system.logger_config import logger


def main():

    try:
        # Parent class object
        employee1 = Employee(
            "EMP001",
            "Arjun",
            50000,
            "Finance"
        )

        # Child class object
        developer1 = Developer(
            "DEV001",
            "Meera",
            75000,
            "Technology",
            "Python",
            5
        )

        # Another child class object
        developer2 = Developer(
            "DEV002",
            "Rahul",
            85000,
            "Technology",
            "Java",
            7
        )

        print("\n========== EMPLOYEE ==========")
        employee1.display_details()

        print("\n========== DEVELOPER 1 ==========")
        developer1.display_developer_details()

        print("\n========== DEVELOPER 2 ==========")
        developer2.display_developer_details()

        # Demonstrating inherited parent method
        print("\n========== INHERITANCE DEMO ==========")

        print("Developer directly calling Employee method:")

        developer1.display_details()

    except InvalidSalaryError as error:
        logger.error(f"Salary error: {error}")
        print("Salary Error:", error)

    except InvalidExperienceError as error:
        logger.error(f"Experience error: {error}")
        print("Experience Error:", error)

    except MissingInformationError as error:
        logger.error(f"Missing information: {error}")
        print("Information Error:", error)

    except Exception as error:
        logger.exception(
            f"Unexpected error occurred: {error}"
        )
        print("Unexpected Error:", error)


if __name__ == "__main__":
    main()