# Andrei Cocan
# Python 3.11.1
# Activity 3 - Tale of the Black Knight
# 01.04.2023 - mm.dd.yyyy

# The random module provides access to random related functions
# The time module provides access to time related functions

import random
import time

goodguy = str(input('\n Enter your Knight\'s Name: '))
goodguy = 'Sir ' + goodguy.title()

# Here, we are assigning the value 'The Black Knight' to the variable badguy
# 1. CHANGE THIS LINE SO THE USER CAN ENTER A VALUE FOR BADGUY

badguy = input(' Enter a name for the bad guy: ')
badguy = 'Sir ' + badguy.title()

# Once Upon A Time...

print('\n ' + goodguy + ', a Knight in search of adventure, is wandering through the enchanted forest one day.')

# 2. WHAT ACTION IS THIS LINE PERFORMING?
# A: It adds a 2 second delay in the script.

time.sleep(2)

print('\n As ' + goodguy + ' reaches a clearing, he encounters the fearsome ' + badguy + '!')

time.sleep(2)

print('\n ' + goodguy + ': You, Sir, are a Blackguard and a coward! I challenge you to a duel!')
print(' ' + badguy + ': I\'mma cut you, fool!')

# Good Guy Health
gghealth = 100

# Bad Guy Health
bghealth = 100

# Fight Sequence Loop

while True:
    


    # 3. EXPLAIN HOW GOODGUY / BADGUY HIT POINTS ARE GENERATED
    # A: Using a random number generator it will generate a value between 1 - 100.
    
    # Good Guy / Bad Guy Hit Points
    
    gghit = random.randint(1, 100)
    bghit = random.randint(1, 100)
    
    # #######################################################

    # 4. WHAT PURPOSE DOES '\n' SERVE?
    # A: It adds an empty new line when printing. (I use this a lot... OCD)
    
    print('\n')

    # 5. FIND & CORRECT THE SYNTAX ERRORS. COMMENT OUT THE INCORRECT LINE AND
    # WRITE THE CORRECT CODE UNDERNEATH
    
    # print goodguy + " rolls a " + gghit
    print(' ' + goodguy + ' rolls a ' + str(gghit))
    # print badguy + " rolls a " + bghit
    print(' ' + badguy + ' rolls a ' + str(bghit))

    # 6. EXPLAIN HOW THE VALUE IN DAMAGE IS CALCULATED
    # A: The hit points generated above are compared and 
    #    the lower hit gets subtracted from the greater hit. 
    #    After this we are left with the damage score of the hit.
    #    The damage score is then subtracted from the oponenets health.
    
    # Damage Calculator
    
    if gghit > bghit:

        damage = gghit - bghit
        bghealth = bghealth - damage
        print(' ' + goodguy + ' strikes ' + badguy + ' for a ' + str(damage) + ' hit!\n')

        if bghealth >= 100:
            print(' ' + badguy + ': Thou hast missed.')
        elif bghealth >= 75:
            print(' ' + badguy + ': Tis but a flesh wound.')
        elif bghealth >= 50:
            print(' ' + badguy + ': Alas! A fair strike! En garde!')
        elif bghealth >= 25:
            print(' ' + badguy + ': Thou art a worthy opponent.')
        elif bghealth < 10:
            print(' ' + badguy + ': I am beaten. Well fought...')
            break
    
    # #######################################################
    
    elif bghit > gghit:

        damage = bghit - gghit
        gghealth = gghealth - damage

        print(' ' + badguy + ' strikes ' + goodguy + ' for a ' + str(damage) + ' hit!\n')

    # 7. CORRECT THE SYNTAX ERROR(S) <-- For this I just fixed them without commenting out the bad lines since it was not mentioned here.
        if gghealth == 100:
            print(' ' + goodguy + ': Thou hast missed.')
        elif gghealth >= 75:
            print(' ' + goodguy + ': Tis but a flesh wound.')
        elif gghealth >= 50:
            print(' ' + goodguy + ': Alas! A fair strike! En garde!')
        elif gghealth >= 25:
            print(' ' + goodguy + ': Thou art a worthy opponent.')
        elif gghealth < 10:
            print(' ' + goodguy + ': I am beaten. Well fought...')
            break

    # #######################################################

# END OF LOOP ###############################################

# 8. PRINT A CONGRATULATORY STATEMENT HERE USING THE NAME OF THE WINNER (GOODGUY OR BADGUY)

if gghealth > bghealth:
    winner = goodguy
else:
    winner = badguy

print('\n End of the Knight Fight')
print(f' {winner} has won this battle!\n') # Here I am testing the use of f-strings that you mentioned to me.

# 9. PART 2
'''
In your own words, answer the following 4 questions on the use of the WHILE Loop in the script from Part 1:

    1. What Condition will end the WHILE Loop? 
        The boolean value that is oposite of the one used to run the while loop.
        In this case 'True' runs the loop, so 'False' would end the loop.
    
    2. How is that Condition handled in the code?
        In this case the break statment is used to end the loop.
        This can be found in the health check if statement when the health points fall bellow 10.

    3. What events happen inside the WHILE Loop?
        The battle takes place in the while loop and the damage is calculated and applied to the health points.

    4. Why are gghealth & bghealth initially set outside the WHILE Loop?
        The health point are initiated outside of the while loop so that they do not get reset during the battle.

'''

# 10. AFTER completing upload your completed script as a .zip file to FSO
