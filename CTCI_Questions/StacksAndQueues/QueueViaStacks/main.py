# Implement a MyQueue class which implements a queue using two stacks.


class MyQueue:
    def __init__(self):
        self.my_queue = []
        self.temp_stack = []

    def is_empty(self):
        return not self.my_queue

    def add(self, item):
        self.my_queue.append(item)

    def remove(self):
        if not self.temp_stack:
            while self.my_queue:
                self.temp_stack.append(self.my_queue.pop())
        return self.temp_stack.pop()

    def print_queue(self):
        print(self.my_queue)


def main():
    my_queue = MyQueue()
    my_queue.add(2)
    my_queue.add(3)
    my_queue.add(4)
    my_queue.add(5)
    my_queue.print_queue()
    print(my_queue.remove())


if __name__ == "__main__":
    main()

