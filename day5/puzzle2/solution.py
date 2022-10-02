import os
import sys
from collections import Counter


def load_data():
    """
    Read the data from input file, return a list of lines
    """
    with open(os.path.join(sys.path[0], "input.txt")) as file:
        lines = [line.replace(" ", "") for line in file.readlines()]
    return lines


class HydrothermalVent:
    def __init__(self, line):
        self.line = line
        self.x_start = 0
        self.y_start = 0
        self.x_end = 0
        self.y_end = 0
        self.is_straight_line = False
        self.vent_coordinates = []
        self.set_coordinates()
        self.get_vents()

    def set_coordinates(self):
        """
        Get the coordinates of where the vent starts and ends, from a str (line)
        Also checks if the vent runs in a straight line, or diagonally
        """
        coord_start, coord_end = self.line.split("->")
        x_start, y_start = coord_start.split(",")
        x_end, y_end = coord_end.split(",")
        self.x_start = int(x_start)
        self.y_start = int(y_start)
        self.x_end = int(x_end)
        self.y_end = int(y_end)
        self.is_straight_line = (self.x_start == self.x_end) or (
            self.y_start == self.y_end
        )

    def get_vents(self):
        """
        Stores a list of lists in self.vent_coordinates, where each list is a set of
        [x, y] coordinates of a vent
        """
        if self.x_start == self.x_end:  # vertical line
            min_y = min(self.y_start, self.y_end)
            max_y = max(self.y_start, self.y_end)
            self.vent_coordinates.extend(
                [self.x_start, y] for y in list(range(min_y, max_y + 1))
            )
        elif self.y_start == self.y_end:  # horizontal line
            min_x = min(self.x_start, self.x_end)
            max_x = max(self.x_start, self.x_end)
            self.vent_coordinates.extend(
                [x, self.y_start] for x in list(range(min_x, max_x + 1))
            )
        else:  # diagonal line
            # get line from left to right
            left_x = min(self.x_start, self.x_end)
            right_x = max(self.x_start, self.x_end)
            if left_x == self.x_start:
                left_x_y, right_x_y = self.y_start, self.y_end
            else:
                left_x_y, right_x_y = self.y_end, self.y_start

            length = right_x - left_x + 1
            if left_x_y < right_x_y:  # line goes up
                for i in range(0, length):
                    self.vent_coordinates.append([left_x + i, left_x_y + i])

            else:  # line goes down
                for i in range(0, length):
                    self.vent_coordinates.append([left_x + i, left_x_y - i])


def count_vents(vents):
    """
    Create a dictionary where each key is an coordinate set,
    and each value is the count
    """
    vent_counts = {}
    for vent in vents:
        # check each individual coordinate,
        # and increase the corresponding counter in vent_counts
        for coord_set in vent.vent_coordinates:
            x = coord_set[0]
            y = coord_set[1]
            if (x, y) in vent_counts:
                vent_counts[(x, y)] += 1
            else:
                vent_counts[(x, y)] = 1
    return vent_counts


if __name__ == "__main__":

    lines = load_data()
    vents = [HydrothermalVent(line) for line in lines]

    vent_counts = count_vents(vents)

    duplicated_vents = 0

    counts = dict(Counter(vent_counts.values()))
    for key in counts:
        if key > 1:
            duplicated_vents += counts[key]

    print("There are {} coordinates with 2 or more vents".format(duplicated_vents))
