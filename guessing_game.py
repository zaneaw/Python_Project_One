import random

welcome_signs = "=" * 43
print("{}\n    WELCOME to Zane's Zany Number Game!   \n{}".format(welcome_signs, welcome_signs))
name = input("\nWhat is your name, contestant? ").title()
hiscore_list = []


def start_game():
    def play_again():
        answer = input("{}, would you like to play again? (Yes / No) ".format(name))
        answer.lower()
        if answer == "yes" or answer == "y":
            print("\nGreat! Try to beat your hiscore of {}!".format(min(hiscore_list)))
            start_game()
            answer
        else:
            print("\nYour hiscore was {}! See you next time!".format(min(hiscore_list)))

    guess_attempts = 1
    random_number = random.randint(1, 10)

    print(random_number)

    print("\nGood luck, {}!".format(name))
    guess = int(input("\nI'm thinking of a number between 1 and 10. Can you guess it? "))

    while True:
        if guess != random_number:
            if guess < 1 or guess > 10:
                guess = int(input("\nTRY AGAIN!\nThe number is between 1 and 10! "))
            elif guess > random_number:
                guess = int(input("\nWRONG!\nThe number is going to be lower! "))
                guess_attempts += 1
            elif guess < random_number:
                guess = int(input("\nWRONG!\nThe number is going to be higher! "))
                guess_attempts += 1
        elif guess_attempts > 1:
            print("CORRECT!\nIt only took you {} attempts to guess the right number!".format(guess_attempts))
            hiscore_list.append(guess_attempts)
            play_again()
            break
        else:
            print("\nNice job, you guessed it on the first try!")
            hiscore_list.append(guess_attempts)
            play_again()
            break


start_game()
