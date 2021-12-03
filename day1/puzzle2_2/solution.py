import os
import sys

directions = []

with open(os.path.join(sys.path[0], "input.txt")) as file:
    for line in file:
        directions.append(line.rstrip())

horizontal_position = 0
depth = 0

for direction in directions:
    if "forward " in direction:
        horizontal_position += int(direction.split("forward ")[1])
    elif "down " in direction:
        depth += int(direction.split("down ")[1])
    elif "up " in direction:
        depth -= int(direction.split("up ")[1])

print("Horizontal position: ", horizontal_position)
print("Depth: ", depth)
print("Horizontal position * depth = ", horizontal_position * depth)
