import time

from stacks import *


def main():
    print(convert_to_base(144758259826592865, 16))


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