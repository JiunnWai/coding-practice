ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'


def get_user_choice():
    # Get user input for their choice of rock, paper, or scissors
    return input()


def get_winning_move(choice):
    # Return the choice that would defeat the one in input
    if choice == ROCK:
        return PAPER
    elif choice == PAPER:
        return SCISSORS
    elif choice == SCISSORS:
        return ROCK


def print_result(winning_choice):
    # Print a message showing the user lost
    print(f"Sorry, but the computer chose {winning_choice}")


if __name__ == '__main__':
    user_choice = get_user_choice()
    winning_choice = get_winning_move(user_choice)
    print_result(winning_choice)
