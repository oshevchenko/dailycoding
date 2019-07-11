# [Hard]
# Given an array of strictly the characters 'R', 'G', and 'B',
# segregate the values of the array so that all the Rs come first,
# the Gs come second, and the Bs come last.
# You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

characters = ['R', 'G', 'B']
# characters = ['B', 'G', 'R']

def partition(A, lo, hi):
    global characters
    pivot = A[hi]
    i = lo
    j = lo
    while j < hi:
        if characters.index(A[j]) < characters.index(pivot):
            # print("swap A[i] with A[j]",i,j)
            x = A[i]
            A[i] = A[j]
            A[j] = x
            i = i + 1
        j+=1
    # print("swap A[i] with A[hi]",i,hi)
    x = A[i]
    A[i] = A[hi]
    A[hi] = x

    return i

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        # print(p, A)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def main():

    # A = [5,3,3,4,1,3,8,2,13,54]
    A = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    quicksort(A, 0, len(A)-1)
    print(A)

main()