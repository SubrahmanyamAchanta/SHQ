"""
Task 7
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a
mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
password every time the user asks for a new password. Include your run-time code in a main method.

Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import string
import random


def generate_password(password_content):
    sample_string = ""
    if password_content["upper_case"]:
        sample_string += string.ascii_uppercase
    if password_content["lower_case"]:
        sample_string += string.ascii_lowercase
    if password_content["digits"]:
        sample_string += string.digits
    if password_content["symbols"]:
        sample_string += string.punctuation
    password = "".join(random.sample(sample_string, password_content["password_length"]))
    return password


def get_user_input():
    length = int(input("Enter the required length of password: "))
    upper_case = int(input("Use UpperCase (ABC) in password? 1 for yes, 0 for no. : "))
    lower_case = int(input("Use LowerCase (abc) in password? 1 for yes, 0 for no. : "))
    digits = int(input("Use Digits (123) in password? 1 for yes, 0 for no. : "))
    symbols = int(input("Use Symbols (#$&) in password? 1 for yes, 0 for no. : "))
    return {
        "password_length": length,
        "upper_case": upper_case,
        "lower_case": lower_case,
        "digits": digits,
        "symbols": symbols
    }


def main():
    try:
        user_input = int(input("Enter 1 to generate a new password, 0 to exit: "))
        while user_input != 0:
            if user_input == 1:
                password_content = get_user_input()
                print(generate_password(password_content))
            else:
                print("Invalid Choice")
            user_input = int(input("Enter 1 to generate another password, 0 to exit: "))

    except ValueError:
        print("Please enter a integer number")


if __name__ == "__main__":
    main()
