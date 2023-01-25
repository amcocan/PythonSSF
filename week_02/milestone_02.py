# Andrei Cocan
# Python 3.11.1
# Milestone 2
# 01.04.2023 - mm.dd.yyyy


# Imports for random generation and time delays.
import random
import time

# Variables for players, scores, and attacks
# pirates_firstlist = ['Steve', 'Bob', 'John', 'Hill']
# pirates_secondlist = ['Jess', 'Lizzy', 'Taylor', 'Natalia']

# Reverted to this list as per the feedback - Thankyou for the feedback btw :)
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

# Dodge beats Parry > Parry beats Thrust > Thrust beats Dodge (This is a note for me to see when building conditionals)
attacks = ['Dodge', 'Parry', 'Thrust']

# I set the scores here so that they don't reset during the game
pirates_fl_score = 0
pirates_sl_score = 0

# Roled the players for the same reason as setting the score before the loop
pirates_fl = str(random.choice(pirates)).title()
pirates_sl = str(random.choice(pirates)).title()

# -------------------------------------------------- Start of loop -------------------------------------------------- 

# This is where I will setup the game loop
while True:

    # The player attacks get generated here
    pirates_fl_atk = random.choice(attacks)
    pirates_sl_atk = random.choice(attacks)

    # This is where I pring out the player attacks
    print(f'\n \'{pirates_fl}\' used {pirates_fl_atk}.')
    print(f' \'{pirates_sl}\' used {pirates_sl_atk}.')

    # Round win check variables (meant to reset every round)
    pfl_rw = 0
    psl_rw = 0

    # I put the conditionals here
    if pirates_fl_atk == pirates_sl_atk: # Response for a draw
        
        print(f' \'{pirates_fl}\' reached a draw with \'{pirates_sl}\'.')

    elif pirates_fl_atk == attacks[0] or pirates_sl_atk == attacks[0]: # Compare attacks to Dodge
    
        if pirates_fl_atk == attacks[1]:
            psl_rw += 1
            
        elif pirates_fl_atk == attacks[2]:
            pfl_rw += 1

        elif pirates_sl_atk == attacks[1]:
            pfl_rw += 1
            
        elif pirates_sl_atk == attacks[2]:
            psl_rw += 1
        
    elif pirates_fl_atk == attacks[1] or pirates_sl_atk == attacks[1]: # Compare attacks to Parry

        if pirates_fl_atk == attacks[0]:
            pfl_rw += 1
            
        elif pirates_fl_atk == attacks[2]:
            psl_rw += 1

        elif pirates_sl_atk == attacks[0]:
            psl_rw += 1
            
        elif pirates_sl_atk == attacks[2]:
            pfl_rw += 1

    # The code above, also handels all comparisons to Thrust attacks, so I don't need to compare further.

    # Round win and scoring takes place here
    if pfl_rw == 1:

        print(f' \'{pirates_fl}\' won this round and gained a point.')
        pirates_fl_score += 1

    elif psl_rw == 1:

        print(f' \'{pirates_sl}\' won this round and gained a point.')
        pirates_sl_score += 1

    # A pause for dramatic effect lolz
    time.sleep(1)

    # End of loop conditional
    if pirates_fl_score == 3 or pirates_sl_score == 3:
        
        break

# -------------------------------------------------- End of loop -------------------------------------------------- 

# This checks for the winner and congratulates them

if pirates_fl_score > pirates_sl_score:

    print(f'\n \'{pirates_fl}\' won three matches against \'{pirates_sl}\'!\n')

else:

    print(f'\n \'{pirates_sl}\' won three matches against \'{pirates_fl}\'!\n')