# This problem was asked by Microsoft.
# Compute the running median of a sequence of numbers.
# That is, given a stream of numbers, print out the median of
# the list so far on each new element.
# Recall that the median of an even-numbered list is the average
# of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5],
# your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def print_running_median(new, array):
    sorted_array=[]
    added = False

    for n in array:
        if not added and new <= n:
            added = True
            sorted_array.append(new)
        sorted_array.append(n)
    if not added:
        sorted_array.append(new)
    array_len = len(sorted_array)
    b = int(array_len/2)

    if array_len%2:
        # odd
        # print(sorted_array, int(len(sorted_array)/2))
        print(sorted_array[b])
    else:
        # even
        print((sorted_array[b-1] + sorted_array[b])/2)
    return sorted_array

def main():
    array = [2, 1, 5, 7, 2, 0, 5]
    sorted_array = []
    for x in array:
        sorted_array = print_running_median(x, sorted_array)

main()

