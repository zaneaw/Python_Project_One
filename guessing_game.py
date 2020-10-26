import sys
import math
import random

print("Welcome to Zane's Zany Number Game!")
name = input("What is your name, contestant? ")
name = name.title()

def start_game():
    print("Good luck, {}".format(name))

start_game()
  
    
#     When the program starts, we want to:
#     ------------------------------------
#     1. Display an intro/welcome message to the player.
#     2. Store a random number as the answer/solution.
#     3. Continuously prompt the player for a guess.
#       a. If the guess greater than the solution, display to the player "It's lower".
#       b. If the guess is less than the solution, display to the player "It's higher".
    
#     4. Once the guess is correct, stop looping, inform the user they "Got it"
#          and show how many attempts it took them to get the correct number.
#     5. Let the player know the game is ending, or something that indicates the game is over.
    
#     ( You can add more features/enhancements if you'd like to. )
#     """
#     # write your code inside this function.



# # Kick off the program by calling the start_game function.
# start_game()l