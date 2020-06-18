import time

from graphs import breadth_first_search
from lists.deques import Deque
from lists.ordered_list import OrderedList
from lists.queues import Queue
from lists.stacks import *
from lists.unordered_lists import *
from searching.hashtable import *
from trees.BinarySearchTree import *
from sorting.quick_sort import quick_sort
from sorting.insertion_sort import insertion_sort


def main():
    print(insertion_sort([12, 54, 6, 32, 78, 4, 23, 1, 76, 8, 0, 43]))


def bst():
    bst = BinarySearchTree()
    bst.__setitem__(29, "Omondi")
    bst.__setitem__(14, "Allaw")
    bst.__setitem__(58, "Ouru")
    print(bst.__getitem__(14))


def hashing():
    animals = HashTable()
    animals[54] = "cat"
    animals[26] = "dog"
    animals[93] = "lion"
    animals[17] = "tiger"
    animals[77] = "bird"
    animals[31] = "cow"
    animals[44] = "goat"
    animals[55] = "pig"
    # animals[20] = "chicken"
    print(animals.slots)

def list_sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + list_sum(list[1:])


def odd_sum(n):
    i = 1
    current = 1
    sum = 0

    while i <= n:
        sum += current
        current += 2
        i += 1
    print(sum)


def ordered_list_test():
    o_list = OrderedList()

    o_list.add(23)
    o_list.add(10)
    o_list.add(38)
    o_list.add(17)
    o_list.add(40)
    o_list.add(32)
    o_list.add(22)
    o_list.add(1000)
    o_list.add(765)
    o_list.add(67)

    o_list.popItem(7)
    o_list.print_all()


def u_list_test():
    u_list = UnorderedList()
    u_list.add(32)
    u_list.add(45)
    u_list.add(34)
    u_list.add(56)
    u_list.add(72)

    u_list.append(1050)

    u_list.append(88)

    u_list.popItem(4)
    u_list.print_all()


def deque_test():
    guys_deque = Deque()
    guys_deque.add_front("Juma")
    guys_deque.add_front("Allan")
    guys_deque.add_rear("Degue")
    guys_deque.add_rear("Otis")
    guys_deque.add_front("Wafule")

    print(guys_deque.items)
    guys_deque.remove_rear()
    print(guys_deque.items)
    guys_deque.remove_front()
    print(guys_deque.items)


def queue_test():
    bank_queue = Queue()
    print(bank_queue.is_empty())
    bank_queue.enqueue("Aleya")
    bank_queue.enqueue("Kassam")
    bank_queue.enqueue("Almasi")
    bank_queue.enqueue("Kibet")
    print(bank_queue.is_empty())
    print(bank_queue.size())
    bank_queue.dequeue()
    bank_queue.dequeue()
    print(bank_queue.size())
    print(bank_queue.items)


def stackify():
    names_stack = Stack()
    print(names_stack.is_empty())
    names_stack.push("Deer")
    names_stack.push("Ngara")
    names_stack.push(8)
    print(names_stack.size())
    print(names_stack.is_empty())
    names_stack.pop()
    print(names_stack.size())


def sum_of_first_n_digits(n):
    start = time.time()
    sum = n * (n + 1) // 2
    end = time.time()
    time_taken = end - start
    print(time_taken)
    return sum


def is_anagram(str, str2):
    print(sorted(str))
    print(sorted(str2))
    if sorted(str) == sorted(str2):
        return True
    return False


def bainari_sach(list, item):
    midpoint = len(list) // 2
    if list[midpoint] == item:
        return True

    if list[midpoint] < item:
        return bainari_sach(list[midpoint + 1:], item)
    return bainari_sach(list[:midpoint], item)


if __name__ == '__main__':
    main()
