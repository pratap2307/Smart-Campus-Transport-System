"""Reusable validation helpers for the Smart Campus Transport System."""

def required_text(*values):
    """Return True when every supplied value is a non-empty string."""
    return all(isinstance(value, str) and value.strip() for value in values)

def positive_integer(value):
    """Return a positive integer or raise ValueError for invalid input."""
    number = int(value)
    if number <= 0:
        raise ValueError("Value must be positive")
    return number
