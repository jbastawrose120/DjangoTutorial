###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

def checkMatch(player, computer):
    for i in range(len(computer)):
        if(player[i] == computer[i]):
            return True
    return False

def checkClose(player, computer):
    for num in player:
        try:
            value = computer.index(num)
        except:
            value = -1;
        if value != -1:
            return True
    return False


digits = list(range(10))
random.shuffle(digits)
#print(digits[:3])
digits = digits[:3]

# Another hint:
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!\n Code has been generated, please guess a 3 digit number.")
#print(guess)
winCheck = False

while(not winCheck):
    guess = input( "What is your guess?")
    guessAsList = [int(d) for d in str(guess)]
    #print("Guess as list: " + str(guessAsList))
    print("Here is the result of your guess: ")

    #Game Logic
    if (guessAsList != digits):
        if checkMatch(guessAsList, digits):
            print("Match!")
        elif checkClose(guessAsList, digits):
            print("Close!")
        else:
            print("Nope!")
    else:
        winCheck = True
        print("\n\nYou are correct!")



    # if(guessAsList != digits):
    #     for i in range(len(digits)):
    #         if(guessAsList[i] != digits[i]):
    #
    #         else:
    #             print("Match")
    # else:
    #     print("Correct!")
    #     winCheck = True



print("Quitting, Thanks for Playing!")

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

#Welcome Code Breaker! Let's see if you can guess my 3 digit number!
#Code has been generated, please guess a 3 digit number
#What is your guess?
