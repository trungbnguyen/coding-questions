# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop and min should all operate in 0(1) time


class Stack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def size(self):
        return len(self.main_stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        if self.is_empty():
            self.min_stack.append(item)
        else:
            self.min_stack.append(min(self.min_stack[self.size() - 1], item))
        self.main_stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Empty stack")
        self.min_stack.pop()
        return self.min_stack.pop()

    def min(self):
        if self.is_empty():
            raise ValueError("Empty Stack")
        min_top = self.min_stack[self.size() - 1]
        return min_top

    def print_stack(self):
        for i in range(len(self.main_stack) - 1, -1, -1):
            print(self.main_stack[i], end='\n')


def main():
    stack = Stack()
    stack.push(10)
    stack.push(198)
    stack.push(7)
    stack.push(99)
    stack.push(100)
    print("Min:", stack.min())
    stack.print_stack()


if __name__ == "__main__":
    main()
