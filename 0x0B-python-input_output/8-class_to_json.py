#!/usr/bin/python3
"""Define python class to JSON funct"""


def class_to_json(obj):
    """Return the dictionary rep of simple data struct"""
    return obj.__dict__
