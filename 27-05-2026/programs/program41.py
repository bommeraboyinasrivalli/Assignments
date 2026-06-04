#Write a Python Program to Remove Punctuation From a String

import string

text = input("Enter a string: ")

for p in string.punctuation:
    text = text.replace(p, "")

print(text)
