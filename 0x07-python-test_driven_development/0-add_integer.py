#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or floats, casting them to integers if necessary.

    Args:
        a: The first integer or float to add.
        b: The second integer or float to add (default: 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
