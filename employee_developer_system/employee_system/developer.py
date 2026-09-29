from employee_system.employee import Employee
from employee_system.exceptions import InvalidExperienceError
from employee_system.logger_config import logger


class Developer(Employee):
    """Child class that inherits from Employee."""

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language,
        experience
    ):

        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        if experience < 0:
            logger.error(
                f"Invalid experience for developer {employee_id}"
            )
            raise InvalidExperienceError(
                "Experience cannot be negative."
            )

        self.programming_language = programming_language
        self.experience = experience

        logger.info(
            f"Developer created successfully: {self.employee_id}"
        )

    def display_developer_details(self):
        """Display employee and developer information."""

        self.display_details()

        print("Programming Language :", self.programming_language)
        print("Experience           :", self.experience, "years")