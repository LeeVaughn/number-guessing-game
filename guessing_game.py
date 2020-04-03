"""
Python Web Development Techdegree
Project 1 - Number Guessing Game

"""
import random

best_score = 0

def start_game():
    global best_score
    # welcome player to the game
    print("Welcome to the Pick a Number game!")

    # best_score = 0

    # show the current high score if the player is playing again
    if best_score > 0:
        print("Your best score so far is {}.".format(best_score))

    # generate a random number within a certain range
    random_number = random.randint(1, 10)
    print(random_number)
    # create a variable to track the number of guesses
    tries = 1

    # prompt use to guess a number
    # convert guess to a number
    # inform the user if their input is a non-number
    while True:
        try:
            current_guess = int(input("Guess a number between 1 and 10: "))
            print(current_guess)
        except ValueError:
            print("Sorry! That is not a valid number. Please try again...")
            continue

        # while guessed number does not equal random number
        # let the player know if their guess is outside the number range
        # let the player know if their guess is outside the number range
            # display "It's lower" if the guess is too high
            # display "It's higher" if the guess is too low
            # increment the counter variable
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

        # Once the player has guessed the number inform the user that they "Got it"
        print("Congratulations! You guessed the number!")
        # Let the player know how many tries it took
        print("It took you {} tries to guess the correct number.".format(tries))
        # ask the player if they would like to play again
            # if yes, increment games and call start_game
            #  if no, let them know the game is over
        try:
            play_again = input("Would you like to play again? (Y/N): ")

            if play_again.lower() == "y":
                if best_score == 0 or best_score > tries:
                    best_score = tries
                start_game()
                break
            elif play_again.lower() == "n":
                print("Thanks for playing!")
                break
            else:
                raise ValueError("Invalid input. Please enter Y or N.")
        except ValueError as err:
            print("{}".format(err))
            play_again = input("Would you like to play again? (Y/N) ")
            # if yes, increment games and call start_game
        # let them know the game is over

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()