# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans
#that represents a board. Each True boolean represents a wall.
#Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate,
# return the minimum number of steps required to reach the end
# coordinate from the start. If there is no possible path,
# then return null.
# You can move up, left, down, and right. You cannot move through walls.
# You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left),
# the minimum number of steps required to reach the end is 7, since we
# would need to go through (1, 2) because there is a wall everywhere
# else on the second row.
M = 4 #rows
N = 4 #columns

board = [[False, False, False, False],
[ True,  True, False,  True],
[False, False, False, False],
[False, False, False, False]]

def coord_is_valid(coord):
    if coord[0] < 0 or coord[0] >= M: return None
    if coord[1] < 0 or coord[1] >= N: return None
    row = board[coord[0]]
    wall = row[coord[1]]
    if wall: return None
    return coord


def move_up(coord):
    # (3,0) > (2,0)
    new_coord = (coord[0]-1, coord[1])
    return coord_is_valid(new_coord)
def move_down(coord):
    # (3,0) > (4,0)
    new_coord = (coord[0]+1, coord[1])
    return coord_is_valid(new_coord)
def move_right(coord):
    # (3,0) > (3,1)
    new_coord = (coord[0], coord[1]+1)
    return coord_is_valid(new_coord)
def move_left(coord):
    # (3,1) > (3,0)
    new_coord = (coord[0], coord[1]-1)
    return coord_is_valid(new_coord)

def variant_len(variant):
    n=0
    while variant:
        n = n + 1
        variant = variant[1]
    return n

def variant_reverse(variant):
    var=[]
    while variant:
        var.append(variant[0])
        variant = variant[1]
    var.reverse()
    return var

def overlap(coord, variant):
    while variant:
        if coord == variant[0]: return True
        variant = variant[1]
    return False

def sortByLength(val):
    return val[0]

moves = (move_up, move_down, move_right, move_left)
def recursive(G, coord, end_coord, parent):
    for m in moves:
        new_coord = m(coord)
        # print(coord, new_coord)
        if new_coord and not overlap(new_coord, parent):
            variant = (new_coord, parent)
            if new_coord == end_coord:
                length = variant_len(variant)
                variant = variant_reverse(variant)
                G.append((length, variant))
                print(length, variant)
            else:
                recursive(G, new_coord, end_coord, variant)
def main(start_coord, end_coord):
    G = []
    recursive(G, start_coord, end_coord, None)
    if len(G):
        G.sort(key=sortByLength)
        solution = G[0]
        return (solution[0])
    else:
        return None


start_coord = (3, 0)
end_coord = (0, 0)
steps = main(start_coord, end_coord)
print("Number of steps to get from", start_coord,"to",end_coord,"is", steps)
