from trees.tree_node import TreeNode


class BinarySearchTree(object):
    TreeNodeClass = TreeNode

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = self.TreeNodeClass(key, val)
        self.size = self.size + 1

    def _put(self, key, val, node):
        if key < node.key:
            if node.left:
                self._put(key, val, node.left)
            else:
                node.left = self.TreeNodeClass(key, val, parent=node)
        else:
            if node.right:
                self._put(key, val, node.right)
            else:
                node.right = self.TreeNodeClass(key, val, parent=node)

    def __getitem__(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.val
        raise KeyError

    def _get(self, key, node):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._get(key, node.left)
        return self._get(key, node.right)

    def __contains__(self, key):
        return bool(self._get(key, self.root))

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
                return
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
            return

        raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        if node.is_leaf() and node.parent is not None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_one_child():
            promoted_node = node.left or node.right

            if node.is_left_child():
                promoted_node.parent = node.parent
                node.parent.left = promoted_node
            elif node.is_right_child():
                promoted_node.parent = node.parent
                node.parent.right = promoted_node
            else:
                node.replace_node_data(promoted_node.key, promoted_node.val, promoted_node.left, promoted_node.right)
        else: #has both children
            successor = node.find_successor()
            if successor:
                successor = node.splice_out()
                node.key , node.val = successor.key, successor.val
