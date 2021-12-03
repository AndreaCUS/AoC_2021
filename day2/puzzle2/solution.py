import os
import sys

directions = []

with open(os.path.join(sys.path[0], "input.txt")) as file:
    for line in file:
        directions.append(line.rstrip())

horizontal_position = 0
depth = 0
aim = 0

for direction in directions:
    units = int(direction.split(" ")[1])
    if "forward " in direction:
        horizontal_position += units
        depth += units*aim
    elif "down " in direction:
        aim += units
    elif "up " in direction:
        aim -= units

print("Horizontal position: ", horizontal_position)
print("Depth: ", depth)
print("Horizontal position * depth = ", horizontal_position * depth)
