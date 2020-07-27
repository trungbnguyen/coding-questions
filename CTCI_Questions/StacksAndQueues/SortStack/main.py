# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is_empty()


class Stack:
    def __init__(self):
        self.stack = []

    def sort(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        elif len(self.stack) == 1:
            return self.stack
        # use insertion sort
        for i in range(1, len(self.stack)):
            key = self.stack[i]
            j = i - 1
            while j >= 0 and key > self.stack[j]:
                self.stack[j + 1] = self.stack[j]
                j -= 1
            self.stack[j + 1] = key
        return self.stack

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")

        popped = self.stack.pop()
        self.stack.pop()
        return popped

    def peek(self):
        return self.stack[-1]

    def print_stack(self):
        print(self.stack)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(15)
    stack.push(8)
    stack.push(52)
    stack.push(9)
    stack.print_stack()
    print(stack.sort())


if __name__ == "__main__":
    main()
