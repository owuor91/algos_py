from collections import deque


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


def hot_potato(names, num):
    queue = deque()
    for name in names:
        queue.appendleft(name)

    while len(queue) > 1:
        for _ in range(num):
            queue.appendleft(queue.pop())

        queue.pop()

        return queue.pop()
