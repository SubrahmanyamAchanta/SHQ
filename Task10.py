"""
Task 10
Please write a program to compress and decompress the string "Music industry hails passage of the Music
Modernization Act".
"""

import gzip

input_str = b'Music industry hails passage of the Music Modernization Act'
file_name = "file.txt.gz"
# Creates a compressed gz file with a text file containing input string.
with gzip.open(file_name, "wb") as fp:
    fp.write(input_str)

with gzip.open(file_name, "rb") as fp:
    output_str = fp.read()

print(output_str)
