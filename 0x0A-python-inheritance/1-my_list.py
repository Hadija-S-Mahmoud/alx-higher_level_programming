#!/usr/bin/python3
"""Defines inherited list of class MyList."""


class MyList(list):
    """Implements the sorted prntng for builtin list class."""

    def print_sorted(self):
        """Prints a list in ascending format."""
        print(sorted(self))
