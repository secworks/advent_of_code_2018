#======================================================================
# Code for solving day 3 of AoC 2018
#======================================================================

VERBOSE = True

#------------------------------------------------------------------
#------------------------------------------------------------------
def load_input(filename):
    my_list = []
    with open(filename,'r') as f:
        for line in f:
            my_list.append(parse_line(line))
    return my_list


#------------------------------------------------------------------
# Extract the claims from the input data.
#------------------------------------------------------------------
def parse_line(line):
    cid, at, coord, size = line.split(" ")
    cid = int(cid[1:])
    x_coord, y_coord = coord.split(",")
    x_coord = int(x_coord)
    y_coord = int(y_coord[:-1])
    x_size, y_size = size.split("x")
    x_size = int(x_size)
    y_size = int(y_size)    
    return (cid, x_coord, y_coord, x_size, y_size)


#------------------------------------------------------------------
#------------------------------------------------------------------
def map_claims(claims):
    # Create a suitable fabric filled with zeros.
    fabric = [[0 for x in range(1000)] for y in range(1000)]    

    # Map all claims on the fabric. 
    for claim in claims:
        cid, x_coord, y_coord, x_size, y_size = claim
        for x in range(x_size):
            for y in range(y_size):
                fabric[x_coord + x][y_coord + y] += 1 
    return fabric


#------------------------------------------------------------------
#------------------------------------------------------------------
def part_one(claims):
    fabric = map_claims(claims)
        
    # Scan the complete fabric after places with multiple claims.
    ctr = 0
    for x in range(1000):
        for y in range(1000):
            if fabric[x][y] > 1:
                ctr += 1
    print('Answer to part 1: %d' % ctr)
    
        
#------------------------------------------------------------------
#------------------------------------------------------------------
def part_two(claims):
    # Get a fabric with the claims mapped onto the fabric.
    fabric = map_claims(claims)
    
    # Walk through the claims again to find the claim
    # for which all coordinates are one
    for claim in claims:
        cid, x_coord, y_coord, x_size, y_size = claim
        non_overlap = True
        cid_found = -2
        for x in range(x_size):
            for y in range(y_size):
                if fabric[x_coord + x][y_coord + y] > 1:
                    non_overlap = False
        if non_overlap:
            cid_found = cid
            
    print('Answer to part 2: %d' % cid_found)


#------------------------------------------------------------------
#------------------------------------------------------------------
print('Answers for day 3:')
my_claims = load_input("puzzle_input_day_3.txt")
part_one(my_claims)

my_claims = load_input("puzzle_input_day_3.txt")
part_two(my_claims)

#======================================================================