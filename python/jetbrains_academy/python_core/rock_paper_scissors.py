import math
import random


RATINGS_FILE = "rating.txt"
USER = "user"
COMPUTER = "computer"
DEFAULT_OPTIONS = ("rock", "paper", "scissors")
RATING = "!rating"
EXIT = "!exit"


def get_username():
    # Ask for the user's name
    username = input("Enter your name: ")
    print(f"Hello, {username}")
    return username


def get_user_score(username, ratings_file):
    # Get the user's score from file containing previous ratings
    user_score = 0

    try:
        ratings = open(ratings_file, "r")
    except FileNotFoundError:
        print("The ratings file does not exist")
    else:
        for line in ratings:
            name, score = line.split()
            if name == username:
                user_score = int(score)
                break
        ratings.close()

    return user_score


def get_game_options():
    # Read input to get a list of options used for the game
    options = input()

    if not options:
        # Use default options
        options = DEFAULT_OPTIONS
    else:
        options = tuple(options.split(","))

    print("Okay, let's start")
    return options


def print_score(score):
    # Print a message to show the user's current score
    print(f"Your rating: {score}")


def get_user_choice(options):
    # Get user input for their choice of action
    user_input = input()
    while user_input not in [*options, RATING, EXIT]:
        print("Invalid input")
        user_input = input()
    return user_input


def get_computer_choice(options):
    # Randomly choose for the computer
    return random.choice(options)


def find_winner(options, user_choice, computer_choice):
    # Evaluate the user and computer's choices and return the winner
    winner = None

    if user_choice != computer_choice:
        # Split the options into 2 halves around the index of user's choice
        index = options.index(user_choice)
        first_half = options[:index]
        second_half = () if user_choice == options[-1] else options[index+1:]

        # User wins against options in the second half of the rearranged list
        second_half_index = math.floor(len(options) / 2)
        rearranged_options = second_half + first_half
        lose_against = rearranged_options[:second_half_index]
        win_against = rearranged_options[second_half_index:]

        if computer_choice in win_against:
            winner = USER
        elif computer_choice in lose_against:
            winner = COMPUTER

    return winner


def calculate_score(score, winner, user_choice, computer_choice):
    # Print a message showing the result of the game
    if winner == USER:
        score += 100
        print(f"Well done. The computer chose {computer_choice} and failed")
    elif winner == COMPUTER:
        print(f"Sorry, but the computer chose {computer_choice}")
    else:
        score += 50
        print(f"There is a draw ({user_choice})")
    return score


if __name__ == '__main__':
    username = get_username()
    score = get_user_score(username, RATINGS_FILE)
    options = get_game_options()

    while True:
        user_choice = get_user_choice(options)

        if user_choice == RATING:
            print_score(score)
        elif user_choice == EXIT:
            print("Bye!")
            break
        elif user_choice in options:
            computer_choice = get_computer_choice(options)
            winner = find_winner(options, user_choice, computer_choice)
            score = calculate_score(score,
                                    winner,
                                    user_choice,
                                    computer_choice)
