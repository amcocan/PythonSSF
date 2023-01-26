# Andrei Cocan
# Python 3.11.1
# Utilities - Milestone 04
# 01.25.2023 - mm.dd.yyyy

# Imports the random library
import random

# Generate a random num between 1 - 10
def randguesser():
    x = random.randrange(1, 11)
    return x

def grabber(y, z):
    x = input(f'\n Please enter {y}.\n [{z}]: ')
    return x
