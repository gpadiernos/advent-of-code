#!/usr/bin/python3

# Advent of code 2019
# Day 01

def calculate_fuel(fuel_mass):
    # recursively calculate the fuel needs to launch a module.
    new_fuel_mass = fuel_mass // 3 - 2
    if new_fuel_mass <= 0:
        return 0
    return new_fuel_mass + calculate_fuel(new_fuel_mass)

#read in masses
with open ('input.txt', 'r') as i:
    mass = [int(module_mass) for module_mass in i.readlines()]

# initial value
simple_fuel_sum = 0
real_fuel_sum = 0

for module_mass in mass:
    fuel = module_mass // 3 - 2
    simple_fuel_sum += fuel
    real_fuel_sum += fuel + calculate_fuel(fuel)

print ("The simple fuel needs are {}".format(simple_fuel_sum))
print("The real fuel needs are {}".format(real_fuel_sum))
