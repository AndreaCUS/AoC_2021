import os
import sys
import numpy as np


def load_data():
    with open(os.path.join(sys.path[0], "input.txt")) as file:
        lines = [line.rstrip() for line in file.readlines()]
    return lines


def get_numbers_called(lines):
    numbers_called = lines[0]
    return numbers_called


def generate_boards(lines):
    output_boards = []
    board_lines = []
    for i in range(2, len(lines)):
        line = lines[i]

        if line == "" or i == len(lines):
            # reached the end of the board, write lines to a board
            board = Board()
            board.add_lines(board_lines)
            output_boards.append(board)
            # start new line collection
            board_lines = []
        else:
            board_lines.append(line)
    return output_boards


class Board:
    def __init__(self):
        self.board = np.zeros((5, 5), dtype=int)
        self.marked = np.zeros((5, 5), dtype=int)

    def add_lines(self, lines):
        print(lines)
        for i in range(5):
            line_numbers = [[int(num) for num in lines[i].split(" ") if num != ""]]
            self.board[i] = line_numbers


if __name__ == "__main__":
    input_lines = load_data()
    numbers_called = get_numbers_called(input_lines)
    boards = generate_boards(input_lines)
