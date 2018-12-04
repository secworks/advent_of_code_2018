#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#======================================================================
# Code for solving day 3 of AoC 2018
#
# Status: Not Done.
#======================================================================

VERBOSE = False 

from operator import itemgetter


#------------------------------------------------------------------
#------------------------------------------------------------------
def load_input(filename):
    my_list = []
    with open(filename,'r') as f:
        for line in f:
            my_list.append(line.strip())
    return my_list

#------------------------------------------------------------------
# Extract the log with events in chronological
# order from the indata.
#------------------------------------------------------------------
def extract_log(lines):
    extracted_log = []
    for line in lines:
        date_time = line[1:17]
        rest = line[18:]
        extracted_log.append(date_time + rest)
    extracted_log.sort()

    if VERBOSE:
        print(extracted_log)
    
    return extracted_log


#------------------------------------------------------------------
# Given a sorted event log we build a db with events for each
# Guard.
#------------------------------------------------------------------
def build_db(event_log):
    event_db = {}
    for event in event_log:
        if "Guard" in event:
            current_guard = int(event.split(" ")[3][1:])
            if current_guard not in event_db:
                event_db[current_guard] = []
        event_db[current_guard].append(event)
    print(event_db[2719])
    return event_db
    
       
#------------------------------------------------------------------
#------------------------------------------------------------------
def part_one():
    event_log = extract_log(load_input("puzzle_input_day_4.txt"))
    time_db = build_db(event_log)
    print("Answer for part one:")


#------------------------------------------------------------------
#------------------------------------------------------------------
def part_two():
    print("Answer for part two:")



#------------------------------------------------------------------
#------------------------------------------------------------------
print('Answers for day 4:')
part_one()
part_two()

#======================================================================
