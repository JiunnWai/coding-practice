def create_empty_state():
    # Create the game state as an empty matrix
    state = []
    for row in range(GRID_SIZE):
        state.append([])
        for _ in range(GRID_SIZE):
            state[row].append(BLANK)
    return state


def print_state(state):
    # Print the game grid
    print("---------")
    for row in range(GRID_SIZE):
        output = "| "
        for col in range(GRID_SIZE):
            output += state[row][col] + " "
        output += "|"
        print(output)
    print("---------")


def players_turn(state, player):
    # Get valid player input and make a move, return new state
    is_valid_coords = False
    while not is_valid_coords:
        coords_string = input("Enter the coordinates: ")
        coords = get_coords(coords_string)

        if is_valid_move(state, coords):
            is_valid_coords = True
            state = make_move(state, coords, player)
    return state


def switch_player(player):
    return O if player == X else X


def check_game_over(state):
    # Check if the game is over and return the game over message
    result = None
    winner = find_winner(state)
    num_blanks = count_chars(state, BLANK)

    if winner in (X, O):
        result = f"{winner} wins"
    elif num_blanks == 0:
        result = "Draw"
    return result


def find_winner(state):
    # Given the state matrix, calculate and return the winner

    # Find horizontal winner
    for row in state:
        if len(set(row)) == 1 and row[0] != BLANK:
            return row[0]

    # Find vertical winner
    vertical_chars = ["" for _ in range(GRID_SIZE)]
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            vertical_chars[col] += state[row][col]

    for col in vertical_chars:
        if len(set(col)) == 1 and set(col) != BLANK:
            return col[0]

    # Find first diagonal winner
    left_right_diagonal_chars = ""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if row == col:
                left_right_diagonal_chars += state[row][col]

    if (len(set(left_right_diagonal_chars)) == 1 and
            left_right_diagonal_chars[0] != BLANK):
        return left_right_diagonal_chars[0]

    # Find second diagonal winner
    reverse_state = [row[::-1] for row in state]
    right_left_diagonal_chars = ""
    for row in range(GRID_SIZE):
        for col in range(2, -1, -1):
            if row == col:
                right_left_diagonal_chars += reverse_state[row][col]

    if (len(set(right_left_diagonal_chars)) == 1 and
            right_left_diagonal_chars[0] != BLANK):
        return right_left_diagonal_chars[0]

    return


def count_chars(state, char):
    # Count how many times the char has appeared in the state
    chars = [char for row in state for col in row if col == char]
    return len(chars)


def get_coords(coords_string):
    # Parse and return a valid or empty coords
    coords = []
    for coord in coords_string.split():
        if coord.isdigit():
            coords.append(int(coord))
    return coords


def is_valid_move(state, coords):
    # Validate if the move is legal or not
    coords_x = coords[0] - 1 if len(coords) > 0 else None
    coords_y = coords[1] - 1 if len(coords) > 1 else None
    is_valid_move = False

    if not coords:
        print("You should enter numbers!")
    elif coords_x > GRID_SIZE - 1 or coords_y > GRID_SIZE - 1:
        print(f"Coordinates should be from 1 to {GRID_SIZE}!")
    elif state[coords_x][coords_y] != BLANK:
        print("This cell is occupied! Choose another one!")
    else:
        is_valid_move = True
    return is_valid_move


def make_move(state, coords, player):
    # Make a move for the player on the game board
    coords_x = coords[0] - 1
    coords_y = coords[1] - 1
    state[coords_x][coords_y] = player
    return state


if __name__ == '__main__':
    GRID_SIZE = 3
    BLANK = " "
    X = "X"
    O = "O"
    INITIAL_PLAYER = X

    # Initialize the game
    state = create_empty_state()
    is_game_over = False
    result = None
    player = INITIAL_PLAYER
    print_state(state)

    # Start the game loop
    while not is_game_over:
        state = players_turn(state, player)
        player = switch_player(player)
        print_state(state)
        result = check_game_over(state)
        is_game_over = bool(result)
    else:
        # Print game result
        print(result)
