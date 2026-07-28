class UsernameAlreadyExistsError(Exception):
    """Raised when trying to create a user with an existing username."""
    pass


class EmailAlreadyExistsError(Exception):
    """Raised when trying to create a user with an existing email."""
    pass