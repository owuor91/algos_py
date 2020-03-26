class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child

    def tree_from_list(self):
        tree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
        print(tree[0])
        print(tree[1])
        print(tree[2])
