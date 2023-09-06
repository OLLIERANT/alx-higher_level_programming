#!/usr/bin/python3
"""
Module to find the peak number in an array of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Method to find peak number in array of unsorted integers
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
