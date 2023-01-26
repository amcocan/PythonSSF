# Andrei Cocan
# Python 3.11.1
# Milestone 04
# 01.25.2023 - mm.dd.yyyy

# A custom utilities external import that imports all from utili_m04.py
from utili_m04 import *


# 4. Create a variable named numbers. 
#    It needs to generate a number between 1 to 10.
#    Put the answer on the next line. 

numbers = randguesser()


# 5. Create a variable named player_name.  
#    It needs to prompt the user to enter his/her name.
#    Put the answer on the next line. 

player_name = grabber('your name', '->').title()


# 6. Create a variable named number_of_guesses and assign 0 to it.
#    Put the answer on the next line. 

number_of_guesses = 0


# 7. Print a string which includes the player_name variable. 
#    It should say: player_name, I am guessing a number between 1 and 10!
#    Put the answer on the next line. 

print(f'\n {player_name}, I am guessing a number between 1 and 10!')


# 8. Create a WHIlE Loop. Give the user 5 attempts to guess the number. 
#    If the number is too low print Your guess is too low. 
#    If the number is too high print Your guess is too high. 
#    Create a break if the user answers it correctly.

loop_count = 5

while loop_count > 0:

    try:

        # Exception handeling.

        guess = int(grabber('a number between 1 and 10', f'{loop_count} tries left. ->'))

        if guess > 10:
            # This throws a custom exception when the condition is met.
            try:
                raise Exception(f'\n Custom exception {guess} > 10')
            except:
                print(f'\n Your guess must be a number 1 - 10, try again.')

        elif guess <= 0:
            # This throws a custom exception when the condition is met.
            try:
                raise Exception(f'\n Custom exception {guess} <= 0')
            except:
                print(f'\n Your guess must be a number 1 - 10, try again.')
        
        else:

            # Conditionals for guesser.

            if guess > numbers:
                loop_count -= 1
                number_of_guesses += 1
                print(f'\n Too high, guess lower.')

            elif guess < numbers:
                loop_count -= 1
                number_of_guesses += 1
                print(f'\n Too low, guess higher.')

            elif guess == numbers:
                loop_count -= 1
                number_of_guesses += 1
                break

    except ValueError:
        print(f'\n Invalid input try again.')


# 9. if/else Statements - Verifying if the user has guessed the number or not.. 
#    If they did...then print a message for them along with the number of tries. 
#    If the player couldnt guess the number at the end...print the number along with a message.

if guess == numbers:
    print(f'\n It took {player_name}, {number_of_guesses} attempts to guess that the secret number was {numbers}.\n')

elif guess != numbers:
    print(f'\n {player_name} did not manage to guess the secret number. The secret number was {numbers}.\n')
