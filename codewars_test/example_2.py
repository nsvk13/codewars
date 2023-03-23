import math
from solution import how_much_water
import codewars_test as test

def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    elif clothes  2*load:
        return 'Too much clothes'
    else:
        water_needed = water * (1.1 ** (clothes - load))
        return round(water_needed, 2)