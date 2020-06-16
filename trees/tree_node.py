class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_leaf(self):
        return not (self.right or self.right)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def has_one_child(self):
        return self.has_any_children() and not self.has_both_children()

    def replace_node_data(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __iter__(self):
        if self is None:
            return

        if self.left:
            for elem in self.left:
                yield elem

        yield self.key

        if self.right:
            for elem in self.right:
                yield elem

    def find_successor(self):
        if self.right:
            return self.right.find_min()

        if self.parent is None:
            return None

        if self.is_left_child():
            return self.parent

        self.parent.right = None
        successor = self.parent.find_successor()
        self.parent.right = self
        return successor

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        else:
            promoted_node = self.left or self.right
            if self.is_left_child():
                self.parent.left = promoted_node
            else:
                self.parent.right = promoted_node
            promoted_node.parent = self.parent
