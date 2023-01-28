"""
Task 9
write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
"""


def binary_search(search_list, key):
    """
    Binary Search using iterative approach as it requires no extra memory space compared to recursive approach will take
    Auxiliary space of O(log n) for storing function call stack. Time complexity for both recursive and iterative
    approach is O(log n).
    """

    left = 0
    right = len(search_list) - 1

    while left <= right:

        mid = (right + left) // 2

        # If key is greater than mid-element, ignore left half
        if search_list[mid] < key:
            left = mid + 1

        # If key is smaller than mid-element, ignore right half
        elif search_list[mid] > key:
            right = mid - 1

        # key is at mid
        else:
            return mid

    # list is traversed, and search key is not found
    return -1


sorted_list = [2, 5, 8, 12, 23, 45, 67, 89]
search_key = 12

index = binary_search(sorted_list, search_key)

if index == -1:
    print("Element is not present in array")
else:
    print("Element is at index", str(index))
