"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""
import random

best_score = 0


def start_game():
    """
    Begins game and handles gameplay functionality

    Prompts user to guess a number between 1 and 10 and an infinite loop runs until they successfully guess the number
    One the player guesses the number another infinite loop runs until they respond to whether they want to play again
    Exceptions are raised for ValueErrors
    """
    # I was running into a local variable referenced before assignment error so I came up with this as a solution
    global best_score
    
    print("\nWelcome to the Pick a Number game!")

    # show the current high score if the player is playing again
    if best_score > 0:
        print("Your best score so far is {}.\n".format(best_score))
    else:
        print("There is no best score currently. Good luck!\n")

    # the number the player will be trying to guess
    random_number = random.randint(1, 10)
    # tracks how many tries the player has made to guess the number
    tries = 1

    # base gameplay
    while True:
        # prompts the player for a number, creates an exception if the input is not a number
        try:
            current_guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Sorry! That is not a valid number. Please try again...\n")
            continue

        # responds based on the players guess
        if current_guess not in range(1, 11):
            print("That number is not between 1 to 10. Please try again...\n")
            continue
        elif current_guess < random_number:
            print("\nIt's higher")
            tries += 1
            continue
        elif current_guess > random_number:
            print("\nIt's lower")
            tries += 1
            continue

        # Once the player has guessed the number...
        print("\nCongratulations! You guessed the number!")
        print("It took you {} tries to guess the correct number.\n".format(tries))

        # sets high score if applicable
        if best_score == 0 or best_score > tries:
            best_score = tries
        break

    # play again?
    while True:
        try:
            play_again = input("Would you like to play again? (Y/N): ")

            if play_again.lower() == "y":
                start_game()
                break
            elif play_again.lower() == "n":
                print("Thanks for playing!")
                break
            else:
                raise ValueError("Invalid input. Please enter Y or N.")
        except ValueError as err:
            print("{}".format(err))


if __name__ == "__main__":
    # Kick off the program by calling the start_game function.
    start_game()
