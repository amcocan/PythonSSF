# 1. Andrei Cocan
# 1. Python 3.11.1
# 1. Milestone 1

# 1. ADD YOUR MULTI LINE COMMENT ON THE NEXT LINE.
""" This is a multi line comment!

Also I have use python before... 
I learned python in highschool.
This is just a refresher for me. """


###### Import the random Module #####
import random

###### Here are your list of Pirates #####
pirates = [
    'Captain William Kidd',
    'Pierre Le Grand',
    'Red Leg Grieves',
    'Edward Low',
    'Calico Jack Rackham',
    'Anne Bonny',
    'Captain Henry Morgan',
    'Black Sam Bellamy',
    'Black Bart Roberts',
    'Edward Blackbeard Teach'
]

# 2. PRINT THE CONTENT OF THE PIRATES LIST TO THE SCREEN HERE
# A: PLACE YOUR ANSWER ON THE NEXT LINE

# Simple Method
print('\n')
print(pirates)
print('\n')

# Better Method
for i in pirates:
    print(' ' + i)


#####  Attacks List #####
attack = ['dodge', 'parry', 'thrust']

# 3. PRINT THE CONTENTS OF THE ATTACK LIST TO THE SCREEN HERE
# A: PLACE YOUR ANSWER ON THE NEXT LINE

# Simple Method
print('\n')
print(attack)
print('\n')

# Better Method
for i in attack:
    print(' ' + i)


##### Choosing the Characters for the fight #####
player = random.choice(pirates)
opponent = random.choice(pirates)

# 4. PRINT THE VALUES STORED IN THE PLAYER AND OPPONENT TO THE SCREEN - Change the lines below to correctly concatenate PLAYER and OPPONENT with
# the variables above so that when the statement prints to screen, the chosen
# character names are shown. 
print('\n Ahoy ye swabs! Prepare for battle!')
print(' ' + player + ' has challenged ' + opponent + ' in one on one combat!')


##### Choosing the attack #####
pattack = random.choice(attack)
oattack = random.choice(attack)

# 5. PRINT THE VALUES STORED IN PATTACK AND OTTACK TO THE SCREEN.
# A: PLACE YOUR ANSWER ON THE NEXT LINE
print('\n ' + pattack)
print(' ' + oattack)

# 6. CREATE A CORRECTLY CONCATENATED STRING THAT CONTAINS PLAYER, OPPONENT, PATTACK & OATTACK
# EXAMPLE: ANNE BONNY ATTACKS WITH DODGE, WHILE EDWARD LOW ATTACKS WITH PARRY
# A: PLACE YOUR ANSWER ON THE NEXT LINE
print('\n ' + player + ' uses ' + pattack + ', while ' + opponent + ' uses ' + oattack + '!\n')
