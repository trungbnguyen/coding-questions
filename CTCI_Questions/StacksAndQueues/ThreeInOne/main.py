# Describe how you could use a single array to implement three stacks.


class NumStacks:

    def __init__(self, number_of_stacks, size):
        self.number_of_stacks = number_of_stacks
        self.size = size

        self.arr = [0] * size

        self.top = [-1] * number_of_stacks

        self.free = 0

        self.next = [i + 1 for i in range(size)]
        self.next[self.size - 1] = -1

    def is_full(self):
        return self.free == -1

    def is_empty(self, stack_number):
        return self.top[stack_number] == -1

    def push(self, item, stack_number):
        if self.is_full():
            return None

        insert = self.free
        self.free = self.next[self.free]
        self.arr[insert] = item

        # assigning the newly inserted item to the top
        # of a specific stack
        self.next[insert] = self.top[stack_number]
        self.top[stack_number] = insert

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return None

        top_of_stack = self.top[stack_number]
        # assign the new top to the next item in the stack
        self.top[stack_number] = self.next[self.top[stack_number]]

        # push the old top to the free stack
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.arr[top_of_stack]

    def print_stack(self, stack_number):
        top = self.top[stack_number]
        while top != -1:
            print(self.arr[top])
            top = self.next[top]


def main():
    num_stacks = NumStacks(3, 12)

    num_stacks.push(5, 0)
    num_stacks.push(80, 0)
    num_stacks.push(9, 0)
    num_stacks.push(1, 1)
    num_stacks.push(6, 1)
    num_stacks.push(24, 2)
    num_stacks.push(15, 2)
    num_stacks.push(7, 2)
    num_stacks.push(681, 2)
    
    print("Popped element from stack 2 is " +
          str(num_stacks.pop(2)))
    print("Popped element from stack 1 is " +
          str(num_stacks.pop(1)))
    print("Popped element from stack 0 is " +
          str(num_stacks.pop(0)))

    num_stacks.print_stack(2)


if __name__ == "__main__":
    main()
