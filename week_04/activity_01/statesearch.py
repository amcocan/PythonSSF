# Andrei Cocan
# Python 3.11.1
# State Capitol Search
# 01.17.2023 - mm.dd.yyyy

# Allow for 5 Searches
# Save Results of search to state_result.txt

#########################################
# IMPORT THE STATES & CAPITOLS
#########################################

# 2. Explain why we start with an empty Dictionary

# A: We start off with an empty dictionary so that we can populate 
#    it with the information found in the file states.txt

# Create Blank Dictionary
states = {}

# 3. Explain how the FOR Loop here is used to import the data
#  and separate it into KEY / VALUE pairs.

# A: The 'for' loop treats the file as a massive array of lines,
#    These lines are then taken one at a time and split on the 
#    delimiter ',' into the following variables: key & val.
#    The content before the ',' is assigned to 'key' while the 
#    content after is assigned to 'val'. 
#    After this the dictionary(states) is populated using the 
#    'key' and pairing 'val' to it.

# Import State & Capitol in the blank Dictionary
f = open('states.txt', 'r')

for line in f:
    (key, val) = line.split(',')
    states[key] = val

f.close()

# User must enter the name of the state to search
print(f'\n STATE SEARCH SCRIPT')
print(f' Please enter the name of 5 states to search for.')

# 4. Create a variable called count with an assigned value of 5

count = 5

##########################################
# LOOP THE SEARCH & WRITE TO EXTERNAL FILE
##########################################

# Open Report file
f = open('state_results.txt', 'w+')

# 5. Describe how the WHILE Loop uses the count variable as a control.

# A: The 'count' variable is defined outside of the while loop 
#    and is used to manipulate the duration of the while loop. 
#    As long as the value of 'count' remains above 0 the while 
#    loop will continue to operate.

# 6. How is the count variable updated?

# A: The variable 'count' is updated inside the while loop 
#    eveytime the user input provided is found in the dictionary 
#    'states'. 'count' is updated using the '-=' method which sets 
#    the value to minus x of the curent value. In this case the 
#    value gets subtracted by 1(one).

# 7. What is the effect?

# A: The effect that 'count -= 1' has on the while loop is that 
#    once the value of 'count' reaches 0(zero) or less the while 
#    loop will stop running. It acts similarly to a 'break' 
#    statement except gives the coder control over how many 
#    times the while loop will iterate.

# 8. Explain how states[search] returns a value.

# A: The variable 'search' is compared to the dictionary 
#    as the {key}, so that means that 'states[search]' 
#    would return the 'val' that is paird with the 'key'(search).

# Use a Loop to run search 5 times
while count > 0:

    search = input('Enter Name of State: ').title()

    # Check the Dictionary for the State / Capitol result
    if search in states:
        print(f' The Capitol of {search} is {states[search]}')
        count -= 1
        print(f' Remaining number of searches: {count}')
        f.write(f"State: {search}, Capitol: {states[search]}")

    else:
        print("You have entered an incorrect value.")
        
count = 5

f.close()

###########################################

# 9. Rewrite the LOOP SEARCH Section above (Lines 85 - 100) to utilize with open()

while count > 0:

    search = input('Enter Name of State: ').title()

    # Check the Dictionary for the State / Capitol result
    if search in states:
        print(f' The Capitol of {search} is {states[search]}')
        count -= 1
        print(f'Remaining number of searches: {count}')

        # I used 'a' to append to the list made by the while loop above this one
        with open('state_results.txt', 'a') as f:
            f.write(f"State: {search}, Capitol: {states[search]}")

    else:
        print("You have entered an incorrect value.")

# 10. Test and confirm your script works before submitting to FSO!