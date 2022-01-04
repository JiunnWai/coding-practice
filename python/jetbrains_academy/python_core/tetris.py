import numpy as np

from typing import List


class Board:
    DEFAULT_BOARD_WIDTH = 10
    DEFAULT_BOARD_HEIGHT = 20
    BLANK_CHAR = '- '

    def __init__(self,
                 width: int = DEFAULT_BOARD_WIDTH,
                 height: int = DEFAULT_BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.board = self._create_board()

    def _create_board(self) -> np.ndarray:
        # Create the board matrix with size width x height, filled with blanks
        return np.full((self.height, self.width), Board.BLANK_CHAR)

    def add_piece(self, piece: 'Piece'):
        # Add the given piece onto the board
        for index in piece.position:
            row = index // self.width
            col = index % self.width
            self.board[row][col] = Piece.PIECE_CHAR

    def reset(self):
        # Reset to an empty board
        self.board = self._create_board()

    def __str__(self) -> str:
        # Return the printable representation of the board
        string = ''
        for row in self.board:
            line = ''.join(row).strip()
            string += line
            string += '\n'
        return string


class Piece:
    PIECE_CHAR = '0 '
    O = ((4, 14, 15, 5),)
    I = ((4, 14, 24, 34), (3, 4, 5, 6))
    S = ((5, 4, 14, 13), (4, 14, 15, 25))
    Z = ((4, 5, 15, 16), (5, 15, 14, 24))
    L = ((4, 14, 24, 25), (5, 15, 14, 13), (4, 5, 15, 25), (6, 5, 4, 14))
    J = ((5, 15, 25, 24), (15, 5, 4, 3), (5, 4, 14, 24), (4, 14, 15, 16))
    T = ((4, 14, 24, 15), (4, 13, 14, 15), (5, 15, 25, 14), (4, 5, 6, 15))

    def __init__(self, piece: str, board_width: int, board_height: int):
        self.piece = piece
        self.board_width = board_width
        self.board_height = board_height
        self.position = self._get_initial_position()
        self.orientation = self.position
        self.row_offset = 0
        self.col_offset = 0

    def _get_initial_position(self) -> List[int]:
        # Return the initial position of the piece
        # ie. Return the value of Piece.I[0]
        current_piece = eval(f'Piece.{self.piece}')
        return current_piece[0]

    def rotate(self):
        # Find which way the piece is oriented and change to the next one
        self.row_offset += 1  # Move the piece down for each command
        possible_orientations = eval(f'Piece.{self.piece}')
        for k, v in enumerate(possible_orientations):
            if self.orientation == v:
                next_orientation_idx = (k+1) % len(possible_orientations)
                self.orientation = possible_orientations[next_orientation_idx]
                break
        self._update_position()

    def move_left(self):
        # Move the piece 1 position to the left and 1 down if possible
        leftmost_col = self.board_width
        for position in self.position:
            leftmost_col = min(leftmost_col, position % self.board_width)

        if leftmost_col > 0:
            self.col_offset -= 1

        self.move_down()
        self._update_position()

    def move_right(self):
        # Move the piece 1 position to the right and 1 down if possible
        rightmost_col = 0
        for position in self.position:
            rightmost_col = max(rightmost_col, position % self.board_width)

        if rightmost_col + 1 < self.board_width:
            self.col_offset += 1

        self.move_down()
        self._update_position()

    def move_down(self):
        # Move the piece 1 position down if possible
        bottommost_row = 0
        for position in self.position:
            bottommost_row = max(bottommost_row, position // self.board_width)

        if bottommost_row + 1 < self.board_height:
            self.row_offset += 1
            self._update_position()

    def _update_position(self):
        # Recalculate the position of the piece based on orientation and offset
        new_position = list(self.orientation)
        for k, v in enumerate(new_position):
            if self.col_offset >= 0:
                v += self.col_offset
            else:
                col_offset = abs(self.col_offset) % self.board_width * -1
                v += col_offset
                if v < 0:
                    v += self.board_width
            v += self.row_offset * self.board_width
            new_position[k] = v
        self.position = new_position


if __name__ == '__main__':
    # Ask for the piece to show
    piece_letter = input()

    # Get board size
    width, height = (int(num) for num in input().split())
    board = Board(width=width, height=height)
    piece = Piece(piece_letter, board.width, board.height)

    # Print the board, then the board with the piece
    print(board)
    board.add_piece(piece)
    print(board)

    # Start loop to get user commands
    while True:
        command = input()

        if command == 'exit':
            break
        elif command == 'rotate':
            piece.rotate()
        elif command == 'left':
            piece.move_left()
        elif command == 'right':
            piece.move_right()
        elif command == 'down':
            piece.move_down()

        board.reset()
        board.add_piece(piece)
        print(board)
