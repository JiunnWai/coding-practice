import random


def initialize_game(stock_pieces,
                    computer_pieces,
                    player_pieces,
                    domino_snake):
    # Generate the domino and split to players and the snake
    first_player = None
    next_player = None
    highest_double = None

    while not first_player:
        reset_game(stock_pieces, computer_pieces, player_pieces, domino_snake)
        generate_domino_set(stock_pieces)
        split_domino_pieces(stock_pieces, computer_pieces, player_pieces)
        first_player, highest_double = find_first_player(computer_pieces,
                                                         player_pieces)

    # Move the highest double from the hand to the snake
    domino_snake.append(highest_double)
    if first_player == COMPUTER:
        computer_pieces.remove(highest_double)
        next_player = PLAYER
    elif first_player == PLAYER:
        player_pieces.remove(highest_double)
        next_player = COMPUTER

    return next_player


def reset_game(stock_pieces, computer_pieces, player_pieces, domino_snake):
    # Reset the game to its initial state
    stock_pieces = []
    computer_pieces = []
    player_pieces = []
    domino_snake = []


def generate_domino_set(stock_pieces):
    # Create all the domino pieces
    top_pip = 0
    bottom_pip = 0

    while bottom_pip <= 6:
        while top_pip <= bottom_pip:
            domino = [top_pip, bottom_pip]
            stock_pieces.append(domino)
            top_pip += 1
        top_pip = 0
        bottom_pip += 1


def split_domino_pieces(stock_pieces, computer_pieces, player_pieces):
    # Randomly split the stock domino pieces to player and computer
    random.shuffle(stock_pieces)
    for _ in range(INITIAL_DOMINOES_PER_PLAYER):
        domino = stock_pieces.pop()
        computer_pieces.append(domino)
        domino = stock_pieces.pop()
        player_pieces.append(domino)


def find_first_player(computer_pieces, player_pieces):
    # Find and return first player (player with highest double)
    first_player = None
    highest_double = None

    highest_computer_double = None
    for d in computer_pieces:
        if d[0] == d[1]:
            if not highest_computer_double:
                highest_computer_double = d
            else:
                if d[0] > highest_computer_double[0]:
                    highest_computer_double = d

    highest_player_double = None
    for d in player_pieces:
        if d[0] == d[1]:
            if not highest_player_double:
                highest_player_double = d
            else:
                if d[0] > highest_player_double[0]:
                    highest_player_double = d

    # Determine who has the highest double
    if highest_computer_double and highest_player_double:
        if highest_computer_double[0] > highest_player_double[0]:
            first_player = COMPUTER
            highest_double = highest_computer_double
        else:
            first_player = PLAYER
            highest_double = highest_player_double
    elif highest_computer_double:
        first_player = COMPUTER
        highest_double = highest_computer_double
    elif highest_player_double:
        first_player = PLAYER
        highest_double = highest_player_double

    return first_player, highest_double


def get_player_move(player_pieces):
    # Prompt the player for a valid and legal move
    move = None
    is_valid_move = False
    is_legal_move = False

    while not is_valid_move or not is_legal_move:
        move = input()

        try:
            move = int(move)
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            if move == 0:
                is_valid_move = True
                is_legal_move = True
            elif 0 < abs(move) <= len(player_pieces):
                is_valid_move = True
                is_legal_move = check_legal_move(domino_snake,
                                                 move,
                                                 player_pieces[abs(move) - 1],
                                                 True)
            else:
                print("Invalid input. Please try again.")

    return move


def get_computer_move(domino_snake, computer_pieces):
    # Prompt user to press enter
    # Computer will try to make a move to play the least favorable piece
    input()

    frequency = {}
    for i in range(7):
        frequency[i] = 0

    for domino in domino_snake:
        top_pip = domino[0]
        bottom_pip = domino[1]
        frequency[top_pip] += 1
        frequency[bottom_pip] += 1

    for domino in computer_pieces:
        top_pip = domino[0]
        bottom_pip = domino[1]
        frequency[top_pip] += 1
        frequency[bottom_pip] += 1

    scores = {}
    for domino in computer_pieces:
        top_pip_score = frequency[domino[0]]
        bottom_pip_score = frequency[domino[1]]
        total_score = top_pip_score + bottom_pip_score
        scores[total_score] = domino

    move = None
    while scores and not move:
        highest_domino = scores.pop(max(scores))

        if check_legal_move(domino_snake, +1, highest_domino, False):
            move = computer_pieces.index(highest_domino) + 1
        elif check_legal_move(domino_snake, -1, highest_domino, False):
            move = computer_pieces.index(highest_domino) * -1 + 1
        else:
            move = 0

    return move


def check_legal_move(domino_snake, move, domino, is_player):
    # Check if the intended move is legal or not and return a boolean
    is_legal_move = False

    if move > 0:
        snake_right_domino_pip = domino_snake[-1][-1]
        is_legal_move = snake_right_domino_pip in domino
    elif move < 0:
        snake_left_domino_pip = domino_snake[0][0]
        is_legal_move = snake_left_domino_pip in domino

    if not is_legal_move and is_player:
        print("Illegal move. Please try again.")
    return is_legal_move


def apply_user_move(stock_pieces, user_pieces, domino_snake, move):
    # Make a move for the user to add the domino to the snake
    if move == 0 and stock_pieces:
        random.shuffle(stock_pieces)
        domino = stock_pieces.pop()
        user_pieces.append(domino)
    elif move > 0:
        domino = user_pieces.pop(abs(move) - 1)
        if domino_snake[-1][-1] == domino[1]:
            domino.reverse()
        domino_snake.append(domino)
    elif move < 0:
        domino = user_pieces.pop(abs(move) - 1)
        if domino_snake[0][0] == domino[0]:
            domino.reverse()
        domino_snake.insert(0, domino)


def check_game_over(stock_pieces,
                    computer_pieces,
                    player_pieces,
                    domino_snake):
    # Check if game over condition is met and try to determine the winner
    is_game_over = False
    winner = None

    if len(computer_pieces) == 0:
        winner = COMPUTER
        is_game_over = True
    elif len(player_pieces) == 0:
        winner = PLAYER
        is_game_over = True
    elif len(stock_pieces) == 0:
        is_game_over = True
    else:
        snake_head = domino_snake[0][0]
        snake_tail = domino_snake[-1][-1]

        if snake_head == snake_tail and domino_snake.count(snake_head) == 8:
            is_game_over = True

    return is_game_over, winner


def change_turn(current_player):
    # Change turn between player and computer
    if current_player == PLAYER:
        return COMPUTER
    elif current_player == COMPUTER:
        return PLAYER


def print_interface(stock_pieces,
                    computer_pieces,
                    player_pieces,
                    domino_snake,
                    next_player):
    # Print the interface showing status of the game
    print("=" * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")

    snake = ""
    if len(domino_snake) < 7:
        for d in domino_snake:
            snake += f"{d}"
    else:
        head = domino_snake[:3]
        tail = domino_snake[-3:]
        for d in head:
            snake += f"{d}"
        snake += "..."
        for d in tail:
            snake += f"{d}"
    print(f"{snake}\n")

    print(f"Your pieces:")
    [print(f"{i}:{v}") for i, v in enumerate(player_pieces, start=1)]

    if next_player == PLAYER:
        print("\nStatus: It's your turn to make a move. Enter your command.")
    elif next_player == COMPUTER:
        print("\nStatus: Computer is about to make a move. "
              "Press Enter to continue...")


def print_game_result(winner):
    # Print a message to show who won
    if winner == PLAYER:
        print("Status: The game is over. You won!")
    elif winner == COMPUTER:
        print("Status: The game is over. The computer won!")
    else:
        print("Status: The game is over. It's a draw!")


if __name__ == '__main__':
    TOTAL_DOMINOES = 28
    INITIAL_DOMINOES_PER_PLAYER = 7
    PLAYER = "player"
    COMPUTER = "computer"

    stock_pieces = []
    computer_pieces = []
    player_pieces = []
    domino_snake = []
    is_game_over = False
    winner = None

    next_player = initialize_game(stock_pieces,
                                  computer_pieces,
                                  player_pieces,
                                  domino_snake)

    while not is_game_over:
        print_interface(stock_pieces,
                        computer_pieces,
                        player_pieces,
                        domino_snake,
                        next_player)

        if next_player == PLAYER:
            move = get_player_move(player_pieces)
            apply_user_move(stock_pieces, player_pieces, domino_snake, move)
        elif next_player == COMPUTER:
            move = get_computer_move(domino_snake, computer_pieces)
            apply_user_move(stock_pieces, computer_pieces, domino_snake, move)
        next_player = change_turn(next_player)

        is_game_over, winner = check_game_over(stock_pieces,
                                               computer_pieces,
                                               player_pieces,
                                               domino_snake)

    print_interface(stock_pieces,
                    computer_pieces,
                    player_pieces,
                    domino_snake,
                    next_player)

    print_game_result(winner)
