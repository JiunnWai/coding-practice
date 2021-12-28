import numpy as np


GRID_SIZE = 4
BLANK_CHAR = '- '
PIECE_CHAR = '0 '

O = [[5, 6, 9, 10]]
I = [[1, 5, 9, 13], [4, 5, 6, 7]]
S = [[6, 5, 9, 8], [5, 9, 10, 14]]
Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]


def create_empty_grid() -> np.ndarray:
    # Create an empty grid as a 2D array of size x size
    grid = []
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            row.append(BLANK_CHAR)
        grid.append(row)
    return np.array(grid)


def print_grid(grid: np.ndarray):
    # Print the given 2D array grid
    string = ''
    for i in grid:
        for j in i:
            string += f'{j}'
        string += '\n'
    print(string)


def print_piece(piece: list):
    # Given a list containing the state of a piece, print the piece
    grid = create_empty_grid()
    for i in piece:
        grid[i // GRID_SIZE][i % GRID_SIZE] = PIECE_CHAR
    print_grid(grid)


if __name__ == '__main__':
    # Ask for the piece to show, ie. T
    piece = input()
    print()

    # Print an empty grid
    empty_grid = create_empty_grid()
    print_grid(empty_grid)

    # Print and rotate the unique pieces
    if piece == 'O':
        for i in range(5):
            print_piece(O[0])
    elif piece == 'I':
        for state in I:
            print_piece(state)
        print_piece(I[0])
    elif piece == 'S':
        for state in S:
            print_piece(state)
        print_piece(S[0])
    elif piece == 'Z':
        for i in range(5):
            print_piece(Z[i%2])
        # for state in Z:
        #     print_piece(state)
        # print_piece(Z[0])
    elif piece == 'L':
        for state in L:
            print_piece(state)
        print_piece(L[0])
    elif piece == 'J':
        for state in J:
            print_piece(state)
        print_piece(J[0])
    elif piece == 'T':
        for state in T:
            print_piece(state)
        print_piece(T[0])
