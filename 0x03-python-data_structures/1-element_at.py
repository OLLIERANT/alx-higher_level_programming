#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrievs an element from my_list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
