# Andrei Cocan
# Python 3.11.1
# Activity 1
# 01.17.2023 - mm.dd.yyyy

# Input / Output

# w write permissions
# w+ write permissions w\create blank doc
# r read only permission
# a append

#######################
# MLB TEAMS
#######################

# 2. The example below uses the old method of opening an external file.
# Convert the open() function below [line 19 - 22 ]to with open().

# Baseball Team Text file import
with open('mlb-teams.txt', 'r') as f:
    mlb = f.read().splitlines()
    f.close()


# 3. Replace the w+ with the appropriate option for appending the file.
with open('mlb-teams.txt', 'a') as f:
    # 4.  Using the f.write() function, add three more teams to the list:
    # [ Seattle Pilots, Washington Senators & Montreal Expos ]
    f.write(f'\nSeattle Pilots')
    f.write(f'\nWashington Senators')
    f.write(f'\nMontreal Expos')
    f.close()

#######################
# HALL OF FAME PLAYERS
#######################

favorite_baseball_player = "Old Hoss Radbourne"

with open("hall_of_fame.txt", 'w+') as f:
    f.write("Bobby Bonds\n")
    f.write("Al Kaline\n")
    f.write("Mickey Mantle\n")
    f.write("Willie Mays\n")

    # 5. Using the f.write() funtion, add the player stored in
    # favorite_baseball_player to the hall_of_fame.txt file
    # Note: You MUST reference the variable in this part.
    f.write(f'{favorite_baseball_player}')

    f.write('\n')

# 6. Replace the r with the appropriate option for appending the file.
with open('hall_of_fame.txt', 'a') as f:
    # 7. Using the f.write() function, add 3 more players the list:
    # [Babe Ruth, Willie Stargell & Roberto Clemente]
    f.write(f'Babe Ruth\n')
    f.write(f'Willie Stargell\n')
    f.write(f'Roberto Clemente')
    f.close()

# 8. Using with open(), place the values stored in hall_of_fame.txt into a variable called hof_players
with open('hall_of_fame.txt', 'r') as f:

    hof_players = f.read().splitlines()
    f.close()

# 9. Write a print statement below with the MLB Team closest to your Home Town.
print(mlb[1])

# 10. Write a print statement to print one of the players stored in the variable hof_players created in step 8.
print(hof_players[3])