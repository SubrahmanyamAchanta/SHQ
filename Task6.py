"""
Task 6
Write the Task 5 titles to the text file.
Extra: Ask the user to specify the name of the output file that will be saved.
"""

from Task5 import get_titles

url_link = "https://news.ycombinator.com/"
file_name = input("Enter a filename")
file_content = get_titles(url_link)

with open(f"{file_name}.txt", 'w') as fp:
    fp.write("\n".join(file_content))
