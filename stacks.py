class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


def balanced_parentheses(parentheses):
    par_stack = []

    for par in parentheses:
        if par == "(":
            par_stack.append(par)
        else:
            try:
                par_stack.pop()
            except IndexError:
                return False

    return len(par_stack) == 0


def convert_to_binary(num):
    binary_stack = []
    while num > 0:
        binary_stack.append(str(num % 2))
        num = num // 2

    binary_str = ""
    for n in range(0, len(binary_stack)):
        binary_str = binary_str + binary_stack.pop()
    print(binary_str)
    # print(''.join(reversed(binary_stack)))


def convert_to_base(num, base):
    DIGITS = '0123456789abcdef'
    base_stack = []
    while num > 0:
        base_stack.append(num % base)
        num = num // base

    new_digits = []
    while base_stack:
        s = DIGITS[base_stack.pop()]
        new_digits.append(s)

    return ''.join(new_digits)
