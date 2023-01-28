"""
Task 10
Please write a program to compress and decompress the string "Music industry hails passage of the Music
Modernization Act".
"""

import zlib
import binascii

input_str = b"Music industry hails passage of the Music Modernization Act"
# used this library https://docs.python.org/3/library/zlib.html
compressed_data = zlib.compress(input_str, 5)
print(f'Original data: {input_str}')
print(f'Compressed data: {binascii.hexlify(compressed_data)}')
decompressed_data = zlib.decompress(compressed_data)
print(f'Decompressed data: {decompressed_data}')