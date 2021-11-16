import random


RATINGS_FILE = "rating.txt"
USER = "user"
COMPUTER = "computer"
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
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

    ratings = open(ratings_file, "r")
    for line in ratings:
        name, score = line.split()
        if name == username:
            user_score = int(score)
            break
    ratings.close()

    return user_score


def print_score(score):
    # Print a message to show the user's current score
    print(f"Your rating: {score}")


def get_user_choice():
    # Get user input for their choice of action
    user_input = input()
    while user_input not in [ROCK, PAPER, SCISSORS, RATING, EXIT]:
        print("Invalid input")
        user_input = input()
    return user_input


def get_computer_choice():
    # Randomly choose for the computer
    return random.choice([ROCK, PAPER, SCISSORS])


def find_winner(user_choice, computer_choice):
    # Evaluate the user and computer's choices and return the winner
    winner = None

    if user_choice == ROCK:
        if computer_choice == ROCK:
            winner = None
        elif computer_choice == PAPER:
            winner = COMPUTER
        elif computer_choice == SCISSORS:
            winner = USER
    elif user_choice == PAPER:
        if computer_choice == ROCK:
            winner = USER
        elif computer_choice == PAPER:
            winner = None
        elif computer_choice == SCISSORS:
            winner = COMPUTER
    elif user_choice == SCISSORS:
        if computer_choice == ROCK:
            winner = COMPUTER
        elif computer_choice == PAPER:
            winner = USER
        elif computer_choice == SCISSORS:
            winner = None

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

    while True:
        user_choice = get_user_choice()

        if user_choice == RATING:
            print_score(score)
        elif user_choice != EXIT:
            computer_choice = get_computer_choice()
            winner = find_winner(user_choice, computer_choice)
            score = calculate_score(score,
                                    winner,
                                    user_choice,
                                    computer_choice)
        else:
            print("Bye!")
            break
