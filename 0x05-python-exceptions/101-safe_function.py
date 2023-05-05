#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely"""
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as error:
        print("Eception: {}".format(error), file=sys.stderr)
        return None
