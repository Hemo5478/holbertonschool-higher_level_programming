#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_made_dict = {}
    for key, value in a_dictionary.items():
        new_made_dict[key] = value * 2
    return (new_made_dict)
