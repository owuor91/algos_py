"""
heap order property, the parent is always less than or equal to the child
while representing heap in a list the left child's position is given by 2p
and the right child's position by 2p +1 where p is the parent's position in the list
the first item in the list is always 0 and is unused in order to facilitate
integer division used to determine the parents position in maitaining the heap order property
"""


class BinaryHeap(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    def percolate_up(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i], self.items[i // 2] = self.items[i // 2], self.items[i]
            i = i // 2

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def min_child(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2] < self.items[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def percolate_down(self, i):
        while i * 2 <= len(self):
            min_child_position = self.min_child(i)
            if self.items[min_child_position] > self.items[i]:
                self.items[min_child_position], self.items[i] = self.items[i], self.items[min_child_position]
            i = min_child_position

    def delete_min(self):
        return_value = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.percolate_down(1)
        return return_value

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.items = [0] + a_list
        while i > 0:
            self.percolate_down(i)
            i = i - 1
