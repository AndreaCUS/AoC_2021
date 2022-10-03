import os
import sys
import numpy as np


def load_data():
    """
    Read the data from input file, return a list of lines
    """
    with open(os.path.join(sys.path[0], "input.txt")) as file:
        lines = file.readlines()
        lines_split = [line.rstrip("\n").split("|") for line in lines]

        lines_processed = []
        for line in lines_split:
            lines_processed.append(
                [line[0].rstrip().split(" "), line[1].rstrip().split(" ")]
            )

    return lines_processed


def count_characters(data):
    character_counter = 0
    for line in data:
        for element in line[1]:
            if len(element) in (2, 4, 3, 7):
                character_counter += 1
    return character_counter


if __name__ == "__main__":

    data = load_data()
    character_counts = count_characters(data)
    print("Number of occurrences: ", character_counts)
