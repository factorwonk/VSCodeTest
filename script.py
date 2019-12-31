import math
import sys
from os import rename

import requests

# which version of python are we using?
print(sys.version)
# where is this version of python located?
print(sys.executable)

# Input commands need to be run in VSCode Terminal
# name = input("Your Name? ")
# print("Hello,", name)


def greet(who_to_greet):
    # test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Abhishek"))

r = requests.get("https://factorwonk.github.io")
print(r.status_code)
