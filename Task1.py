"""
Task 1
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first 
and last elements of the given list. 
For practice, write this code inside a function.
"""


def list_slicer(input_list):
    """to slice and get first and last element from list."""
    try:
        if len(input_list) == 0:
            return "List is empty"
        output = input_list[::len(input_list)-1]
        return output  # alternatively we can simply return [input_list[0], input_list[-1]]
    except ValueError:
        # Exception handling when only 1 element present in input list
        return "List must contain at least 2 elements"


def main():
    """Used functions as it was mentioned in question"""
    input_list = [5, 10, 15, 20, 25]
    sliced_list = list_slicer(input_list)
    print(sliced_list)


main()
