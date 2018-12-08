#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#======================================================================
# Code for solving day 5 of AoC 2018
#======================================================================

VERBOSE = True


#------------------------------------------------------------------
#------------------------------------------------------------------
def load_input(filename):
    with open(filename,'r') as f:
        content = f.read()
    return content.strip()


#------------------------------------------------------------------
#------------------------------------------------------------------
def check_pair(s1, s2):
    if ((s1.isupper() and s2.isupper()) or
         (s1.islower() and s2.islower())):
        return False
    return s1.upper() == s2.upper()


#------------------------------------------------------------------
#------------------------------------------------------------------
def compress(s):
    print("Length before compress: %d" % (len(s)))
    diff = -1
    while diff != 0:
        curr_len = len(s)
        i = 0
        while i < (len(s) -1):
            if check_pair(s[i], s[i + 1]):
                s = s[:i] + s[i + 2:]
                i += 2
            else:
                i += 1
        diff = len(s) - curr_len

    print("Length after compress: %d" % (len(s)))
    return len(s)


#------------------------------------------------------------------
#------------------------------------------------------------------
def remove_chars(ch, s):
    i = 0
    while i < (len(s) -1):
        if s[i].upper() == ch.upper():
            s = s[:i] + s[i + 1:]
        i += 1
    return s


#------------------------------------------------------------------
#------------------------------------------------------------------
def part_one():
    print("Performing part one.")
    my_input = load_input("puzzle_input_day_5.txt")
    min_size = compress(my_input)
    print("Answer for part one: %d" % min_size)



#------------------------------------------------------------------
#------------------------------------------------------------------
def part_two():
    print("Performing part two.")
    my_input = load_input("puzzle_input_day_5.txt")

    # Build db for all chars in the input
    chars = {}
    for ch in my_input:
        if ch.upper() not in chars:
            chars[ch.upper()] = 0

    # For each char we generate a new input with the char removed.
    # Then we compress it and stor the compressed length.
    minlen = len(my_input)
    for ch in chars:
        print("Compressing for char %s" % (ch.upper()))
        new_input = remove_chars(ch, my_input)
        chars[ch] = compress(new_input)
        if chars[ch] < minlen:
            minlen = chars[ch]

    print("Answer for part two: %d" % minlen)



#------------------------------------------------------------------
#------------------------------------------------------------------
print('Answers for day 5:')
#part_one()
part_two()

#======================================================================
