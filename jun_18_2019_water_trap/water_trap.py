# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents
# a two-dimensional elevation map where each element is unit-width
# wall and the integer is the height. Suppose it will rain and
# all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map
# in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of
# water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the
# first index, 2 in the second, and 3 in the fourth index (we
# cannot hold 5 since it would run off to the left), so we can
# trap 8 units of water.

def find_gap_at_level(level, el_map):
    slice = []
    total_gap = 0
    total_brick = 0
    for n in el_map:
        if n > level:
            slice.append(1)
            total_brick += 1
        else:
            slice.append(0)
            total_gap += 1
    # print(slice)
    if not total_brick:
        return (0,0)

    while not slice[0]:
        del(slice[0])
        total_gap -= 1
    while not slice[-1]:
        del(slice[-1])
        total_gap -= 1

    return (total_gap, total_brick)

def find_water_units(el_map):
    i = 0
    total = 0
    while True:
        (total_gap, total_brick) = find_gap_at_level(i, el_map)
        if not total_gap and total_brick < 3: break
        i += 1
        total += total_gap
    # print(total)
    return total



def main():
    # el_map = [1]
    # el_map = [1,0,1]
    # el_map = [0, 2, 1, 10,9,10]
    el_map = [3, 0, 1, 3, 0, 5]
    # el_map = [3, 0, 1, 3, 0, 5, 3, 2, 3]
    # el_map = [1,2,3, 0, 1, 3, 0, 5, 4, 3, 2, 3]
    print(el_map)
    total = find_water_units(el_map)
    print(total)
    return

main()



