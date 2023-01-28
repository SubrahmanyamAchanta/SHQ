"""
Task 8
If we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
If the following email address is given as input to the program: tom@SecurityHQ.com
Then, the output of the program should be: securityhq
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

import re

regex = '(?<=@)[^.]+'
input_email = input("Enter an email address: ")
matches = re.findall(regex, input_email)
# used .lower as sample output in question is in lowercase
print(matches[0].lower())
