"""
Python Web Development Techdegree
Project 1 - Number Guessing Game

"""
import random

best_score = 0

def start_game():
    # I was running into a local variable referenced before assignment area so I came up with this as a solution
    global best_score
    
    print("Welcome to the Pick a Number game!")

    # show the current high score if the player is playing again
    if best_score > 0:
        print("Your best score so far is {}.".format(best_score))
    else:
        print("There is no best score currently. Good luck!")

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
            print("Sorry! That is not a valid number. Please try again...")
            continue

        # responds based on the players guess
        if current_guess < 1 or current_guess > 10:
            print("That number is not between 1 to 10. Please try again...")
            continue
        elif current_guess < random_number:
            print("It's higher")
            tries += 1
            continue
        elif current_guess > random_number:
            print("It's lower")
            tries += 1
            continue

        # Once the player has guessed the number...
        print("Congratulations! You guessed the number!")
        print("It took you {} tries to guess the correct number.".format(tries))

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
            # play_again = input("Would you like to play again? (Y/N) ")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()