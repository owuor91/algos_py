from collections import deque


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


def is_palindrome(characters):
    word_deque = deque(characters)

    while len(word_deque) > 1:
        first = word_deque.popleft()
        last = word_deque.pop()

        if first != last:
            return False

    return True
