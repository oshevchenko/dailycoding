# This problem was asked by Google.
#
# Implement locking in a binary tree.
# A binary tree node can be locked or unlocked only if
# all of its descendants or ancestors are not locked.
#
# Design a binary tree node class with the following methods:
#
# is_locked, which returns whether the node is locked
# lock, which attempts to lock the node. If it cannot be
# locked, then it should return false.
# Otherwise, it should lock it and return true.
# unlock, which unlocks the node. If it cannot be unlocked,
# then it should return false. Otherwise, it should unlock
# it and return true.
# You may augment the node to add parent pointers or any
# other property you would like. You may assume the class
# is used in a single-threaded program, so there is no need
# for actual locks or mutexes. Each method should run in O(h),
# where h is the height of the tree.

class Node(object):
    """docstring for Node"""
    def __init__(self, data, parent=None):
        super(Node, self).__init__()
        self.locked = False
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent
    def insert(self, data):
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data, self)
        else:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data, self)

    def lookup(self, data):
        if self.data == data:
            return self
        else:
            if self.left:
                node = self.left.lookup(data)
                if node:
                    return node
            if self.right:
                node = self.right.lookup(data)
                if node:
                    return node
        return None

    def is_locked(self):
        return self.locked
    def check_locked_descendants(self):
        if self.is_locked():
            return True
        if self.left:
            if self.left.check_locked_descendants():
                return True
        if self.right:
            if self.right.check_locked_descendants():
                return True
        return False
    def check_locked_ancestors(self):
        parent = self.parent
        while parent:
            if parent.is_locked():
                return True
            parent = parent.parent
        return False
    def lock(self, dryrun=False):
        if self.is_locked():
            return False
        if self.check_locked_ancestors():
            return False
        if self.check_locked_descendants():
            return False
        if not dryrun:
            self.locked = True
        return True

def main():
    data=[
            50,
            40, 60,
            35, 45, 55, 65,
            32, 37, 42, 47, 52, 57, 62, 67,

            150,
            140, 160,
            135, 145, 155, 165,
            132, 137, 142, 147, 152, 157, 162, 167
        ]

    root = Node(100)
    for d in data:
        root.insert(d)
# 32  37  42  47  52  57  62  67  132  137  142  147  152  157  162  167
#   35      45      55      65       135       145       155       165
#       40              60                 140                 160
#             50                                      150
#                                 100
    print("Let's lock 160  (False, True, True, False)")
    print(root.lookup(160).is_locked())
    print(root.lookup(160).lock())
    print(root.lookup(160).is_locked())
    print(root.lookup(160).lock())
    print("Dryrun lock, should be all False:")
    print(root.lookup(100).lock(True))
    print(root.lookup(150).lock(True))
    print(root.lookup(155).lock(True))
    print(root.lookup(165).lock(True))
    print(root.lookup(152).lock(True))
    print(root.lookup(157).lock(True))
    print(root.lookup(162).lock(True))
    print(root.lookup(167).lock(True))
    print("Dryrun lock, should be all True:")
    print(root.lookup(140).lock(True))
    print(root.lookup(135).lock(True))
    print(root.lookup(145).lock(True))
    print(root.lookup(50).lock(True))
    print(root.lookup(40).lock(True))
    print(root.lookup(60).lock(True))
    print(root.lookup(35).lock(True))
    print(root.lookup(45).lock(True))
    print("Let's lock 35 (False, True, True, False)")
    print(root.lookup(35).is_locked())
    print(root.lookup(35).lock())
    print(root.lookup(35).is_locked())
    print(root.lookup(35).lock())
    print("Dryrun lock, should be all False:")
    print(root.lookup(32).lock(True))
    print(root.lookup(37).lock(True))
    print(root.lookup(40).lock(True))
    print(root.lookup(50).lock(True))
    print("Dryrun lock, should be all True")
    print(root.lookup(42).lock(True))
    print(root.lookup(45).lock(True))
    print(root.lookup(52).lock(True))
    print(root.lookup(55).lock(True))
    print(root.lookup(132).lock(True))
    print(root.lookup(140).lock(True))


main()
