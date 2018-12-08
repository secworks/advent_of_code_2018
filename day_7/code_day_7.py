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
def find_root(parts):
    dependents = set()
    for first, second in parts:
        if second not in dependents: 
            dependents.add(second)
    print(dependents)

    for first, second in parts:
        if first not in dependents:
            return first
    

#------------------------------------------------------------------
#------------------------------------------------------------------
def part_one():
    print("Performing part one.")
    my_input = load_input("puzzle_input_day_7.txt")

    parts = set()
    for first, second in my_input:
        parts.add(first)
        parts.add(second)
    print("All parts:")
    print(parts)

    root = find_root(my_input)
    print("root part is: %s" % root)
    
    part_order = root
    
    
    
    print("Answer for part one: %s" % part_order)


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
