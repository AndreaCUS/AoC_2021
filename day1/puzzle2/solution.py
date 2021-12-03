import os
import sys

depths = []

with open(os.path.join(sys.path[0], "input.txt")) as file:
    for line in file:
        depths.append(int(line.rstrip()))

counter = 0

for index, val in enumerate(depths):
    if index > 2:
        if val > depths[index - 3]:
            counter += 1

print(counter)
