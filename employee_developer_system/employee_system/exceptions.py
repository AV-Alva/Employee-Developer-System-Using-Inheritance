class InvalidSalaryError(Exception):
    """Raised when salary is zero or negative."""
    pass


class InvalidExperienceError(Exception):
    """Raised when experience is negative."""
    pass


class MissingInformationError(Exception):
    """Raised when required employee information is missing."""
    pass