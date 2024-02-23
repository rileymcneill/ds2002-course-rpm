#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

os.environ["YEAR"] = "Third-year"
os.environ["AGE"] = "20"
os.environ["HOMETOWN"] = "New York City"

YEAR = input('What year are you? ')
AGE = input('How old are you? ')
HOMETOWN = input('Where are you from? ')

print(YEAR)
print(AGE)
print(HOMETOWN)
