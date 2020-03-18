import time

from deques import Deque
from lists import *
from queues import Queue
from stacks import *


def main():
    u_list = UnorderedList()
    u_list.add(32)
    u_list.add(45)
    u_list.add(34)
    u_list.add(56)
    u_list.add(72)

    u_list.insert(6, 1007)

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
    time_taken  = end -start
    print(time_taken)
    return sum

def is_anagram(str, str2):
    print(sorted(str))
    print(sorted(str2))
    if sorted(str) == sorted(str2):
        return True
    return False

if __name__=='__main__':
    main()