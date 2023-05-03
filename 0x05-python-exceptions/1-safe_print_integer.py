#!/usr/bin/python3
def safe_print_integer(value):
    """Writes a function that prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
