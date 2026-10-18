def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y


def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If x, y or z is not a number.
    """
    # original version did not check the inputs so I added it here
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise ValueError("All inputs must be numbers.")
    total_sum = x + y + z
    return total_sum


def fun5(x, y):
    """
    Divides x by y.
    Args:
        x (int/float): Number to divide.
        y (int/float): Number to divide by.
    Returns:
        float: Result of x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is 0.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def fun6(x, y):
    """
    Raises x to the power of y.
    Args:
        x (int/float): Base number.
        y (int/float): Exponent.
    Returns:
        int/float: x to the power of y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y


def fun7(numbers):
    """
    Finds the average of a list of numbers.
    Args:
        numbers (list): List of int/float values.
    Returns:
        float: Average of the numbers.
    Raises:
        ValueError: If the list is empty or has something that is not a number.
    """
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non empty list.")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All items in the list must be numbers.")
    return sum(numbers) / len(numbers)


# f1_op = fun1(2,3)
# f2_op = fun2(2,3)
# f3_op = fun3(2,3)
# f4_op = fun4(f1_op,f2_op,f3_op)
