import os
import sys
import numpy as np


def load_data():
    """
    Read the data from input file, return a list of lines
    """
    with open(os.path.join(sys.path[0], "input.txt")) as file:
        lines = file.readlines()
        initial_fish_str = lines[0].rstrip("\n").split(",")
        initial_fish = [int(fish) for fish in initial_fish_str]
    return initial_fish


def grow_fish(fish):
    next_day_fish = {
        "adults": {6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
        "babies": {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    }
    for key in fish["adults"]:
        if key == 0:
            next_day_fish["babies"][8] += fish["adults"][0]  # make babies
            next_day_fish["adults"][6] += fish["adults"][0]  # reset fish to 6
        else:
            next_day_fish["adults"][key - 1] += fish["adults"][key]  # grow fish

    for key in fish["babies"]:
        if key == 0:
            next_day_fish["babies"][8] += fish["babies"][0]  # make babies
            next_day_fish["adults"][6] += fish["babies"][0]  # make an adult
        else:
            next_day_fish["babies"][key - 1] += fish["babies"][key]  # grow fish
    return next_day_fish


if __name__ == "__main__":
    days_to_breed = 80 # puzzle part 1
    # days_to_breed = 256 # puzzle part 2
    initial_fish_states = load_data()
    fish = {
        "adults": {6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
        "babies": {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    }
    for i in initial_fish_states:
        fish["adults"][i] += 1
    for i in range(days_to_breed):
        fish = grow_fish(fish)
    fish_count = 0
    for value in fish["adults"].values():
        fish_count += value
    for value in fish["babies"].values():
        fish_count += value
    print("Fish count: ", fish_count)
