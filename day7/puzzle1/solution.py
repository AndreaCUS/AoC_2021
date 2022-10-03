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
    individual_costs = [abs(position - ideal_position) for position in crab_positions]
    total_fuel_costs = int(sum(individual_costs))
    return total_fuel_costs

if __name__ == '__main__':
    crab_positions = load_data()
    ideal_position = int(statistics.median(crab_positions))
    print("The position the crabs must align to is {}".format(str(ideal_position)))
    fuel_spend = get_fuel_cost(crab_positions, ideal_position)
    print("The total fuel cost to align will be {}".format(str(fuel_spend)))
