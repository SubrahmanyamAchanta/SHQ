"""
Task2
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
My name is Michele
Then I would see the string:
Michele is name My
shown back to me.
"""


def str_word_rev(input_str):
    """Split a long sentence into a list of words and reverse the list"""
    str_split = str.split(" ")
    str_split.reverse()
    return str_split


def main():
    input_str = input("Input string: ")
    print(f'Output string: {" ".join(str_word_rev(input_str))}')


main()
