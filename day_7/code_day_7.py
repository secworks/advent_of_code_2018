#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#======================================================================
# Code for solving day 7 of AoC 2018
#======================================================================

VERBOSE = True


#------------------------------------------------------------------
#------------------------------------------------------------------
def load_input(filename):
    my_input = []
    with open(filename,'r') as f:
        for line in f:
            my_input.append((line[5], line[36]))
    return my_input


#------------------------------------------------------------------
#------------------------------------------------------------------
def part_one():
    print("Performing part one.")
    my_input = load_input("puzzle_input_day_7.txt")

    my_db = {}
    for first, second in my_input:
        if not first in my_db:   
            my_db[first] = []
        else:
            my_db[first].append(second)
    print(my_db)
    
    print("Answer for part one: ")


#------------------------------------------------------------------
#------------------------------------------------------------------
def part_two():
    print("Performing part two.")
    print("Answer for part two: ")

#------------------------------------------------------------------
#------------------------------------------------------------------
print('Answers for day 5:')
part_one()
part_two()

#======================================================================
