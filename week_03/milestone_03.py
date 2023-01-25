# Andrei Cocan
# Python 3.11.1
# Pirate Swashbuckle Fight Milestone 3
# 01.05.2023 - mm.dd.yyyy

# 1. Import the utilities file

from utili import * # This imports everything from utili.py and removes the need for the 'utili.{function}' to be used

# 2. Import the pirates.txt file

pirates = importing('pirates.txt') # This uses utili to import file with all the pirates

# dodge > parry > thrust > dodge
attack =['dodge', 'parry', 'thrust']

# 3. Use the utilites to randomly pick pirates for player and opponent

player = randomizer(pirates)
opponent = randomizer(pirates)

# 4. Add a while loop so that the pirates are not the same

while player == opponent:
    opponent = randomizer(pirates)

print(f'\n Advast ye swabs, a fight betwixt {player} & {opponent} \'tis bout to commence! ')

pscore = 0
oscore = 0
gameover = False

# Game loop
while gameover == False:

    # This has changed for milestone 3. The game will still end when the player or opponent reaches 3. 
    if pscore >= 3:
        print(f'\n {player} has vanquished {opponent}')
        print(f' Hip hip huzzah!\n')
        gameover = True
        break
    elif oscore >= 3:
        print(f'\n {opponent} has vaquished {player}')
        print(f' Oh Captain, my Captain!\n')
        gameover = True
        break
    
    # 5. Exception - Add a while True and exception. 
    # Example: the player attack variable should allow the user to pick between the different types     

    # This is a bool variable used for the while loop below
    validChoice = False

    # Exceptions loop here
    while validChoice == False:
        
        try: # Try and catch exceptions with the users choice

            # This prompts the player to choose an attack 
            pattack = int(input(f'\n Choose a move:\n [0] Dodge\n [1] Parry\n [2] Thrust\n [3] Random\n\n [Choice]: '))

        except ValueError: # ValueError caught here
            print(f'\n Please make a valid choice.')


    # 6. Player only - Create an if/elif statement to set the number entry to the correct attack.
        
        try: # Try and catch exceptions

            # Contitionals for player choice and corect attack pairing
            if pattack == 0:
                pattack = attack[0]
                validChoice = True
                break
            
            elif pattack == 1:
                pattack = attack[1]
                validChoice = True
                break

            elif pattack == 2:
                pattack = attack[2]
                validChoice = True
                break

            elif pattack == 3:
                pattack = randomizer(attack)
                validChoice = True
                break

        except NameError: # NameError caught here
            print(f'\n Your invalid choice produced this message.')

    # The program randomly picks the attack for the opponent
    oattack = randomizer(attack)

    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    
    while pattack == oattack:
        oattack = randomizer(attack)

    print(f'\n {player} attacks with a {pattack}')
    print(f' {opponent} attacks with a {oattack}')

    # 8. Change your if/elif statment from milestone 2. Use the and to compare the attacks. All attacks must be used correctly.

    if pattack == attack[0] or oattack == attack[0]: # Compare attacks to Dodge
    
        if pattack == attack[1]:
            oscore += 1
            
        elif pattack == attack[2]:
            pscore += 1

        elif oattack == attack[1]:
            pscore += 1
            
        elif oattack == attack[2]:
            oscore += 1
        
    elif pattack == attack[1] or oattack == attack[1]: # Compare attacks to Parry

        if pattack == attack[0]:
            pscore += 1
            
        elif pattack == attack[2]:
            oscore += 1

        elif oattack == attack[0]:
            oscore += 1
            
        elif oattack == attack[2]:
            pscore += 1
        
    # 9. Print a string that includes the player and the players score.

    print(f'\n {player} has a score of {pscore}.')

    # 10. Print a string that includes the opponent and the opponents score.

    print(f' {opponent} has a score of {oscore}.')
