from unordered_lists import *


class OrderedList(UnorderedList):

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            elif current.value > item:
                return False
            current = current.next

        return False

    def add(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        new_node = Node(item)
        if previous == None:
            new_node.next, self.head = self.head, new_node
        else:
            previous.next, new_node.next = new_node, current
