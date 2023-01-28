"""
Task 3
Take two lists, say for example these two:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Extra:
1. Randomly generate two lists to test this
2. Write this in one line of Python
"""

import random


def common_elements(a, b):
    """converting lists into sets and finding intersection. Sets will be easier to operate on, when elements order and
    duplicates need not be preserved"""
    return list(set(a).intersection(b))


def main():
    """generating random sized (size:1-20) lists and filling with random elements in range 1 to 100"""
    a = [random.randrange(1, 100, 1) for i in range(random.randint(1, 20))]
    b = [random.randrange(1, 100, 1) for i in range(random.randint(1, 20))]
    print(f"List 1 : {a}")
    print(f"List 2 : {b}")
    print(common_elements(a, b))


main()
