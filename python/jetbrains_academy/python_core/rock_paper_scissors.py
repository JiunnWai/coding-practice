import random


USER = "user"
COMPUTER = "computer"
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"


def get_user_choice():
    # Get user input for their choice of rock, paper, or scissors
    return input()


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


def print_result(winner, user_choice, computer_choice):
    # Print a message showing the result of the game
    if winner == USER:
        print(f"Well done. The computer chose {computer_choice} and failed")
    elif winner == COMPUTER:
        print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print(f"There is a draw ({user_choice})")


if __name__ == '__main__':
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = find_winner(user_choice, computer_choice)
    print_result(winner, user_choice, computer_choice)
