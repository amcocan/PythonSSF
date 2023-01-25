# Andrei Cocan
# Python 3.11.1
# Activity 1
# 01.05.2023 - mm.dd.yyyy

###################################################################################################

import time

# Custom Functions
# 2. DESCRIBE HOW THE INCLUDED countdown() FUNCTION WORKS

# A: The countdown function takes in a number and subtracts 1 
#    from it every second untill it's value drops bellow 0 and 
#    prints it to the screen.

def countdown(n):
    while n >= 0:
        print(f' {n}')
        time.sleep(1)
        n -= 1

##################################################################################################

# Self Destruct Sequencer

# This is the custom function created to handle all of the Self Destruct
# features needed. There are a few steps involved in the process, so take a few
# moments to study how this function works and think about ways to make it better.
def self_destruct(x):

    # Set Destruct Codes
    authorized_test = '000-Destruct-0'
    authorized_final = '000-Destruct-1'

    # 3. CREATE VARIABLES (SIMILAR TO ABOVE) FOR THE COMMANDING OFFICER'S CODE (co_code)
    # EXECUTIVE OFFICER'S CODE (xo_code) & CHIEF ENGINEER'S CODE (ce_code)
    # Write your code here
    co_code = '111A-Destruct'
    xo_code = '21A2B-Destruct'
    ce_code = '31B2B-Destruct'

##################################################################################################

    # Consider the following print statements. Could they be combined into a single print
    # statement and get the same result? (Answer: Yes) There are many ways to resolve
    # issues in scripting. You get to decide what works best for your script.

    # Display Self Destruct Warning
    print('\n --------------------- WARNING! ----------------------')
    print(' You have initiated the USR ARES Self Destruct Program')
    print(' -----------------------------------------------------')
    print('\n You must provide Authorized Initiate Code to Proceed.')

##################################################################################################
    
    # Request Authorized Rank

    # 4. EXPLAIN THE SIGNIFICANCE OF THE int() FUNCTION IN THE FOLLOWING LINE:
    rank = int(input('\n Select Correct Rank:\n [1] Commanding Officer\n [2] Executive Officer\n [3] Chief Engineer\n\n RANK: '))
    
    # A. This is to ensure that the input is of type integer 
    #    so that it will work with the conditional below.

##################################################################################################

    # Because we're expecting the user to enter a number above, the conditional statement
    # below is needed to convert those numbers into something more useful. Doing this helps
    # reduce the risk of the user introducing bad data into the script.

##################################################################################################

    # Retrieve Rank Initiate Code

##################################################################################################

    # Commanding Officer

    if rank == 1:
        code = co_code
        print('\n Commanding Officer Confirmed.')

    # Executive Officer

    elif rank == 2:
        code = xo_code
        print('\n Executive Officer Confirmed.')

    # Chief Engineer

    elif rank == 3:
        code = ce_code
        print('\n Chief Engineer Confirmed.')

    else:
        print('\n You are not authorized to initial Self Destruct.')

##################################################################################################

    # Enter Self Destruct Code: 000-Destruct-0 or 000-Destruct-1

##################################################################################################

    # Set Supplied Rank Code
    initiate = input('\n Enter Self Destruct Confirmation Code: ')

    # Compare Rank Codes
    if initiate == code:

        print('\n Self Destruct Initiate Code: ACCEPTED')
        final_code = input('\n Enter Activation Code: ')

        if final_code == authorized_final:
            print('\n Destruct Sequence Confirmed.')

            # 5. EXPLAIN THE SIGNIFICANCE OF X
            print(f' {x} seconds to Self Destruct.')

            # A. 'x' is the parameter or also known as the placeholder variable
            #    that is passed into the self_destruct() function.

            print(' ALL HANDS ABANDON SHIP - THIS IS NOT A DRILL')
            countdown(x)
            print(' Have a nice day!')
            print(' BOOM!\n')

        elif final_code == authorized_test:
            print('\n Destruct Sequence Test Order Confirmed.')
            print(' THIS IS A DRILL - THIS IS A DRILL')
            print(f' Timer Set to: {x} seconds.\n')

        else:
            print('\n Destruct Sequence Aborted.\n')

##################################################################################################

    # Program Ends

##################################################################################################

# Self Destruct
timer = int(input('\n Enter Countdown Length (in seconds): '))
self_destruct(timer)



# 6. LIST THE LOCAL VARIABLES AND GLOBAL VARIABLES USED THROUGHOUT THIS SCRIPT
# A. 
#       authorized_final
#       authorized_test
#       co_code
#       xo_code
#       ce_code
#       rank
#       code
#       initiate
#       final_code
#       timer
#       n
#       x
# 

# 7. LIST THE BUILT IN FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. The Built-in functions used are print(), and input().

# 8. LIST THE MODULE FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. The module function used belong to the time module and is sleep().

# 9. LIST THE CUSTOM FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. The custom functions used are countdown() and self_destruct().