#!/usr/bin/python3
"""Defines object attributes lookup funct."""


def lookup(obj):
    """Return a list of object's available attributes."""
    return (dir(obj))
