"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
from sys import argv
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("sys.argv--")
print(sys.argv)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS Platform--")
print(sys.platform)

print("sys.version")
print(sys.version)

# print("OS nmae--")
# print(os.name)

# Print out the version of Python you're using:
# YOUR CODE HERE


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

print("OS name--")
print(os.name)
# Print the current process ID
# YOUR CODE HERE
print("the current process ID")
print(os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("current working directory")
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE

import system
print("OS system--")
print(platform.system())



# from random import randint