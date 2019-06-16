# This problem was asked by Google.

# Given a singly linked list and an integer k,
# remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one
# pass is prohibitively expensive.

# Do this in constant space and in one pass.

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def remove_element(self, k):
        if not self.headval:
            print("Error! Empty list.")
            return
        p_list = self.headval
        p_list_del = self.headval
        delete_last = False
        if k == 0:
            k = 1
            delete_last = True
        for i in range(k):
            p_list = p_list.nextval
            if not p_list:
                if delete_last and i == 0:
                    self.headval = None
                    return
                else:
                    print("Error! k is greater than the length of the list!")
                    return
        while True:
            if p_list.nextval == None:
                # delete p_list_del element
                if (delete_last):
                    p_list_del.nextval = None
                    break
                else:
                    next_after_del = p_list_del.nextval
                    p_list_del.dataval = next_after_del.dataval
                    p_list_del.nextval = next_after_del.nextval
                    break
            else:
                p_list = p_list.nextval
                p_list_del = p_list_del.nextval

    def print_long_list(self):
        if not self.headval:
            print("Error! Empty list.")
            return
        n = self.headval
        i = 0
        while True:
            print("i",i,"dataval:",n.dataval)
            i += 1
            if n.nextval:
                n = n.nextval
            else:
                break

def main():
    linked_list = SLinkedList()
    linked_list.headval = Node(0)
    for i in range(5):
        n = Node(i+1)
        n.nextval = linked_list.headval
        linked_list.headval = n
    print("Print the full list")
    linked_list.print_long_list()
    to_be_removed = 5
    linked_list.remove_element(to_be_removed)
    print("Print the full list after removing:",to_be_removed)
    linked_list.print_long_list()

    to_be_removed = 0
    linked_list.remove_element(to_be_removed)
    print("Print the full list after removing:",to_be_removed)
    linked_list.print_long_list()

main()
