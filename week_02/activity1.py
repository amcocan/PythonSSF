# Andrei Cocan
# Python 3.11.1
# Activity 1 - Part 1
# 01.04.2023 - mm.dd.yyyy

# Variables

name = input('\n Enter your name: ')
age = float(input(' Enter your age: ')) # Professor I used a float over an int here in case people want to estimate their age.
citlen = float(input(' Enter the length of your citizenship in \'YEARS\': ')) # Professor I used a float over an int here in case people want to estimate their citizenship.

# If Statement

if age >= 30 and citlen >= 9:
    print('\n ' + name.title() + ' is eligible for both the \'House Of Representatives\' and \'Senate\'.\n')
elif age >= 25 and citlen >= 7:
    print('\n ' + name.title() + ' is eligible for the \'House Of Representatives\' only.\n')
else:
    print('\n ' + name.title() + ' is not eligible to serve.\n')