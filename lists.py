class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def search(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.value == item:
                return True
            current_node = current_node.next
        return False

    def remove(self, item):
        current_node = self.head
        previous_node = None
        while True:
            if current_node.value == item:
                break
            previous_node, current_node = current_node, current_node.next

        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next

    def append(self, item):
        pass

    def insert(self, position, item):
        pass

    def index(self, item):
        pass

    def pop(self):
        pass

    def pop(self, position):
        pass
