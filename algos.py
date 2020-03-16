import time

def main():
    stackify()

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

class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.size()==0

    def pop(self):
        return self.items.pop()
        #self.items[0:len(self.items)-2]

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

if __name__=='__main__':
    main()