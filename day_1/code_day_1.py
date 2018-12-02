# Code for solving day1 of AoC 2018

VERBOSE = False

def load_list(filename):
    my_list = []
    with open(filename,'r') as f:
        for line in f:
            sign = line[0]
            value = int(line[1:])
            my_list.append((sign, value))
    return my_list


def update_acc(acc, sign, value):
        if sign == '-':
            acc -= value
        else:
            acc += value
        return acc


def update_ptr(ptr, listlen, loops):
    ptr += 1
    if ptr == listlen:
        ptr = 0
        loops += 1
    return loops, ptr    


def part_one(list):
    acc = 0
    for (sign, value) in list:        
        acc = update_acc(acc, sign, value)
    print("The answer to part one is: %d" % acc)


def part_two(list):
    acc = 0
    ptr = 0

    ctr = 0
    loops = 0

    listlen = len(list)
    acc_values = set()

    while acc not in acc_values:
        acc_values.add(acc)
        (sign, value) = list[ptr]
        acc = update_acc(acc, sign, value)
        loops, ptr = update_ptr(ptr, listlen, loops)
        ctr += 1
        if VERBOSE:
            print("Value nr %d: %d" % (ctr, acc))
            
    print("The answer to part two is: %d" % acc)
    if VERBOSE:
        print("Number of loops: %d" % loops)
        

my_list = load_list('puzzle_input_day_1.txt')
part_one(my_list)
part_two(my_list)
