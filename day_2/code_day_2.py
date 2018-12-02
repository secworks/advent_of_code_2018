# Code for solving day 2 of AoC 2018

VERBOSE = False

def load_input(filename):
    my_list = []
    with open(filename,'r') as f:
        for line in f:
            my_list.append(line)
    return my_list


def part_one(input):
    two_ctr = 0
    three_ctr = 0
    
    for word in input:
        two = False
        three = False
        ctr_list = [0] * 256

        for ch in word:
            ctr_list[ord(ch)] += 1
        
        for ctr in ctr_list:
            if ctr == 2:
                two = True
            if ctr == 3:
                three = True
        
        if two:
            two_ctr += 1
        if three:
            three_ctr += 1
    
    result = two_ctr * three_ctr
    print('Answer to part 1: %d' % result)


def calc_diff(str1, str2):
    ctr = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            ctr += 1
    return ctr
    

def find_common_string(str1, str2):
    common = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            common = common + str1[i]
    return common

        
def part_two(input):
    str1 = ''
    str2 = ''
    for i in range(len(input) - 1):
        ptr = i + 1
        while ptr < len(input):
            if calc_diff(input[i], input[ptr]) == 1:
                str1 = input[i]
                str2 = input[ptr]
            ptr += 1
    print("Answer to part 2: %s" % find_common_string(str1, str2))
                    

test_data_part_1 = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
test_data_part_2 = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']


print('Answers for day 2:')
my_input = load_input('puzzle_input_day_2.txt')
part_one(my_input)
part_two(my_input)
