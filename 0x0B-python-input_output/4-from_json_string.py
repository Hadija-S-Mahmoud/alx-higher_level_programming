#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON to object funct"""
import json


def from_json_string(my_str):
    """Return python object rep of JSON string"""
    return json.loads(my_str)
