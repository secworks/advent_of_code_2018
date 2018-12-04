#======================================================================
# Code for solving day 3 of AoC 2018
#======================================================================

VERBOSE = True

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
#------------------------------------------------------------------
def parse_sort(lines):
    extracted_log = []
    parsed_log = []
    for line in lines:
        rest = line[18:]
        date, time = (line[1:17]).split(" ")
        extracted_log.append(date + time + rest)
    extracted_log.sort()
    print(extracted_log)
    return parsed_log


#------------------------------------------------------------------
#------------------------------------------------------------------
def part_one():
    guard_log = parse_sort(load_input("puzzle_input_day_4.txt"))
    print(guard_log)
    print("Answer for part one:")

#------------------------------------------------------------------
#------------------------------------------------------------------
def part_two():
    print("Answer for part one:")



#------------------------------------------------------------------
#------------------------------------------------------------------
print('Answers for day 4:')
part_one()
part_two()

#======================================================================
