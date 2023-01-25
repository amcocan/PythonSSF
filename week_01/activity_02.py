# Andrei Cocan
# Python 3.11.1
# Activity 2


####### Part 1 #######
# Strings

# This initializes two variables of type string.
city = 'cape canaveral'
nickname = 'thrusters'

# String Methods
# This will print: Welcome to cape canaveral home of the Thrusters
print("Welcome to " + city + " home of the " + nickname.capitalize())

# Print to screen
# This will prompt the user for an input of type string (their name),
# and print: Introducing the latest Thrusters player, [users previous input with the fisrt char capitolized]
name = input("Enter Name: ")
print("Introducing the latest " + nickname.title() + " player, " + name.title())


####### Part 2 #######

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# print("The colors in the Rainbow are: ')
print('\n\nThe colors in the Rainbow are: ')
for color in colors:
#    print(color))
    print(color)


# The following errors took place because of the use of missmacthed quotes on line 27
# and an aditional ')' on line 30

# String literal is unterminated
# "(" was not closed


####### Part 3 #######

var1 = '\nThis is a string\n'
var2 = 2
var3 = ['\nThis', 'is', 'a', 'list']
var4 = ('\nThis', 'is', 4, 'tuple\n')
var5 = {'apple', 'pear', 'orange', 'bannana'}
var6 = input('\n\nEnter a string: ')
var7 = int(input('Enter an integer: '))

print(var1)
print(var2)
for i in var3:
    print(i)
for i in var4:
    print(i)
for i in var5:
    print(i)
print('\nThe string you entered is: ' + var6)
print('\nThe integer you entered is: ' + str(var7) + '\n')