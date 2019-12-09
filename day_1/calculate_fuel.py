from math import floor


def calculate_fuel(mass: int) -> int:
    return max(floor(mass / 3) - 2, 0)


with open("./input.txt", "r") as f:
    masses = [l.strip() for l in f.readlines()]
    # print(sum([calculate_fuel(int(mass)) for mass in masses]))  # puzzle 1

    total_fuel = 0
    for mass in masses:
        module_fuel = calculate_fuel(int(mass))
        unaccounted_fuel = module_fuel

        while unaccounted_fuel > 0:
            unaccounted_fuel = calculate_fuel(unaccounted_fuel)
            module_fuel += unaccounted_fuel
        total_fuel += module_fuel
    print(total_fuel)
