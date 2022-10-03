import sys
import os
import statistics


def load_data():
    """
    Read the data from input file, return a list of lines
    """
    with open(os.path.join(sys.path[0], "input.txt")) as file:
        lines = file.readlines()
        input_str = lines[0].rstrip("\n").split(",")
        puzzle_input = [int(fish) for fish in input_str]
    return puzzle_input


def get_fuel_cost(crab_positions, ideal_position):
    individual_costs = []
    for position in crab_positions:
        steps = abs(position - ideal_position)
        # Gauss formula for sum of consecutive numbers:
        # sum = (n / 2)(first number + last number)
        cost = (steps / 2) * (1 + steps)
        individual_costs.append(cost)
    total_fuel_costs = int(sum(individual_costs))
    return total_fuel_costs


def get_ideal_position(crab_positions):
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    lowest_cost = 0
    lowest_cost_position = None
    for position in range(min_position, max_position + 1):
        cost = get_fuel_cost(crab_positions, position)
        if not lowest_cost_position:  # this is the first position
            lowest_cost_position = position
            lowest_cost = cost
        else:
            if cost < lowest_cost:
                lowest_cost_position = position
                lowest_cost = cost

    return lowest_cost_position, lowest_cost


if __name__ == "__main__":
    crab_positions = load_data()
    ideal_position, ideal_cost = get_ideal_position(crab_positions)
    print(
        "The ideal position is {} and it costs {} fuel units.".format(
            str(ideal_position), str(ideal_cost)
        )
    )
