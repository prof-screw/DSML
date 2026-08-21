def divide(a, b):
    """Return the quotient of a and b.

    Raises
    ------
    ZeroDivisionError
        If b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b