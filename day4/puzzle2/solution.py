import os
import sys
import numpy as np


def load_data():
    with open(os.path.join(sys.path[0], "input.txt")) as file:
        lines = [line.rstrip() for line in file.readlines()]
        lines.append([""])
    return lines


def get_numbers_called(lines):
    numbers_called = [int(number) for number in lines[0].split(",")]
    return numbers_called


def generate_boards(lines):
    output_boards = []
    index = 2
    for i in range(0, len(lines) // 6):
        board = Board()
        board.add_lines(lines[index : index + 5])
        output_boards.append(board)
        index += 6
    return output_boards


class Board:
    def __init__(self):
        self.board = np.zeros((5, 5), dtype=int)
        self.matched_numbers = np.zeros((5, 5), dtype=int)

    def add_lines(self, lines):
        for i in range(5):
            line_numbers = [int(num) for num in lines[i].split(" ") if num != ""]
            self.board[i] = line_numbers

    def check_number(self, number):
        if number in self.board:
            matches = np.where(self.board == number)
            self.matched_numbers[matches[0], matches[1]] = 1
            self.board[matches[0], matches[1]] = 0

    def check_winner(self):
        winner = False
        score = None
        if (True in (self.matched_numbers == 1).all(axis=0)) or (
            True in (self.matched_numbers == 1).all(axis=1)
        ):
            winner = True
            score = self.check_score()
        return winner, score

    def check_score(self):
        score = self.board.sum()
        return score


if __name__ == "__main__":
    input_lines = load_data()
    numbers_called = get_numbers_called(input_lines)
    boards = generate_boards(input_lines)
    boards_left = list(range(0, len(boards)))
    last_winner_found = False

    for number in numbers_called:
        for index, board in enumerate(boards):
            if index in boards_left:
                board.check_number(number)
                winner, score = board.check_winner()
                if winner and len(boards_left) == 1:
                    print("Winning board found. Final score: ", str(score * number))
                    last_winner_found = True
                    break
                elif winner:
                    boards_left.remove(index)
        if last_winner_found:
            break
