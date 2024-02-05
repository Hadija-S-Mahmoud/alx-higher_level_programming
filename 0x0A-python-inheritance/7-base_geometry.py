#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Rep of base geometry."""

    def area(self):
        """Not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation of a param as an integer.

        Args:
            name (str): name of the param.
            value (int): param to validate.
        Raises:
            TypeError: value is not an integer.
            ValueError: value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
