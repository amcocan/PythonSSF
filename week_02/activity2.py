# Andrei Cocan
# Python 3.11.1
# Activity 2
# 01.04.2023 - mm.dd.yyyy

####### Part 1 #######
print('\n')

# This is a for loop that will iterate ten times with the first value being 1. The result should print 1 - 10.
for x in range(1,11):
    print(x)

####### Part 2 #######
print('\n')

zoo = ['Lion', 'Zebra', 'Giraffe', 'Hippo']

for animal in zoo:
    # Missmatching quotes.
    # if animal == "Lion':
    if animal == 'Lion':
        # Missing '(' and ')'
        # print "Alex the " + animal
        print('Alex the ' + animal)
    elif animal == 'Zebra':
        # Missing '(' and ')' and had variable 'animal' capitolized.
        # print "Marty the " + Animal
        print('Marty the ' + animal)
    elif animal == 'Giraffe':
        # Missing '(' and ')' and had variable 'animal' misspelled.
        # print "Melman the " + animals
        print('Melman the ' + animal)
    # This was not an error but it is better to have as an else statement since you know it is the last item in the list.
    # elif animal == 'Hippo':
    else:
        # Missing '(' and ')'
        # print "Gloria the " + animal
        print('Gloria the ' + animal)

####### Part 3 #######
print('\n')

import random

# Code Name Lists
alpha = ['Crimson', 'Phantom', 'Zephyr', 'Palisade', 'Skyfall']
omega = ['Whirlwind', 'Gatecrasher', 'Iceberg', 'Zealot', 'Element']

# CREATE FOR LOOP HERE
# HINT: The print function below needs to loop 5 times. In order to receive credit, you must use a FOR Loop. 

for x in range(0, 5):
    print(f"Operation: {random.choice(alpha)} {random.choice(omega)}") # I noticed that this is an f-string!