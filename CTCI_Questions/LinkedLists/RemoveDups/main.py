# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
from random import randint


class Node(object):
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    # Constructor
    def __init__(self, head=None, size=None):
        self.head = head
        self.size = size

    # Display
    def __str__(self):
        representation = []
        curr = self.head
        while curr:
            representation.append(str(curr.data))
            curr = curr.next
        return ' -> '.join(representation)

    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def insert_tail(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            temp = Node(data)
            while curr.next:
                curr = curr.next
            curr.next = temp

    def generate(self):
        for _ in range(10):
            self.insert_tail(randint(0, 9))

    def insert_multiple(self, data):
        for v in data:
            self.insert_tail(v)

    def search(self, data):
        if self.head is None:
            raise ValueError("List is empty")

        curr = self.head
        while curr:
            if curr.data == data:
                return True
            else:
                curr = curr.next
        return False

    def delete_1(self, data):
        if self.head is None:
            return self.head

        curr = self.head
        prev = None

        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            prev = curr
            curr = curr.next

    def delete_2(self, data):
        if self.head is None:
            return self.head

        curr = self.head
        # Edge case
        if curr.data == data:
            self.head = curr.next

        # The rest
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            else:
                curr = curr.next


def remove_dups1(llist, prev=None):
    head = llist.head
    curr = llist.head
    hash = {}

    while curr:
        if curr.data in hash:
            prev.next = curr.next
        elif curr.data in hash and curr.next is None:
            prev.next = None
        else:
            hash[curr.data] = curr.data
        prev = curr
        curr = curr.next
    return head


def remove_dups2(llist, data):
    head = llist.head
    curr = llist.head
    runner = llist.head

    while curr:
        prev = runner
        runner = runner.next

        if runner and runner.data == curr.data:
            prev.next = runner.next
            runner = runner.next

        if runner is None:
            curr = curr.next
            runner = curr
    return head


def main():
    llist = LinkedList()
    llist.generate()
    print(llist)
    # remove_dups1(llist)
    # print(llist)
    remove_dups2(llist, 3)
    print(llist)


if __name__ == "__main__":
    main()
