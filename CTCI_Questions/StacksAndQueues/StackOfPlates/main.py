# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life,
# we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure
# SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack
# once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically
# to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.


class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def is_empty(self):
        return not self.stacks

    def push(self, item):
        if self.is_empty():
            self.stacks.append([item])
        else:
            # check if the current stack has reached its capacity
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Empty Stack")

        popped = self.stacks[-1][-1]
        self.stacks[-1].pop()

        return popped

    def pop_at(self, index):
        if self.is_empty():
            raise ValueError("Empty Stack")
        elif index > len(self.stacks):
            raise NameError("Index out of range")
        popped = self.stacks[index][-1]
        self.stacks[index].pop()
        if not self.stacks[index]:
            del self.stacks[index]

        return popped

    def print_stack(self):
        print(self.stacks)


def main():
    stacks = SetOfStacks(3)
    stacks.push(2)
    stacks.push(4)
    stacks.push(1)
    stacks.push(9)
    stacks.push(10)
    stacks.push(8988)
    stacks.push(51)
    stacks.push(6)
    stacks.push(18)
    stacks.print_stack()
    stacks.pop()
    stacks.pop()
    stacks.print_stack()
    stacks.pop_at(0)
    print(stacks.pop_at(2))
    stacks.print_stack()


if __name__ == "__main__":
    main()
