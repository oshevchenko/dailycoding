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
            A[i], A[j] = A[j], A[i]
            i = i + 1
        j+=1
    # print("swap A[i] with A[hi]",i,hi)
    A[i], A[hi] = A[hi], A[i]
    return i

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def main():
    A = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    quicksort(A, 0, len(A)-1)
    print(A)

main()