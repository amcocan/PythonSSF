# Andrei Cocan
# Python 3.11.1
# Activity 1 - Part 2
# 01.04.2023 - mm.dd.yyyy

# Variables

score = float(input('\n Enter a score between \'0\' and \'100\' to see it\'s place on the grade scale: ')) # Professor I used a float over an int here in case people have a score like '74.5'

# If Statement

if score > 100 or score < 0: # I added this if statement to check and make sure that the score entered is between 0 and 100.
    print('\n You are trolling, get it together.\n')
else:
    if score >= 95:
        print('\n This is an \'A+\'!\n')
    elif score >= 90:
        print('\n This is an \'A\'!\n')
    elif score >= 85:
        print('\n This is an \'B+\'!\n')
    elif score >= 80:
        print('\n This is an \'B\'!\n')
    elif score >= 75:
        print('\n This is an \'C\'!\n')
    elif score >= 70:
        print('\n This is an \'D\'!\n')
    else:
        print('\n This is an \'F\'!\n')