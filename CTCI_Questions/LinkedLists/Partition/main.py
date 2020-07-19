# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
# than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements less than x
# (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between
# the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from random import randint


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, size=None):
        self.head = head
        self.size = size

    def __str__(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        return ' -> '.join(res)

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
            while curr.next:
                curr = curr.next
            temp = Node(data)
            curr.next = temp

    def generate(self):
        for _ in range(10):
            self.insert_tail(randint(0, 9))

    def insert_multiple(self, data):
        for v in data:
            self.insert_tail(v)

    def search(self, data):
        if self.head is None:
            raise ValueError("The list is empty")
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            else:
                curr = curr.next
        return False

    def delete1(self, data):
        if self.head is None:
            return self.head

        curr = self.head
        prev = None

        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    self.head = curr.next
            prev = curr.next
            curr = curr.next

    def delete2(self, data):
        if self.head is None:
            return self.head

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            else:
                curr = curr.next


def partition(ll, x):
    dummy1, dummy2 = Node(0), Node(0)
    curr1, curr2 = dummy1, dummy2
    head = ll.head

    while head:
        if head.data < x:
            curr1.next = head
            curr1 = curr1.next
        else:
            curr2.next = head
            curr2 = curr2.next
        head = head.next

    curr2.next = None
    curr1.next = dummy2.next

    return dummy1.next


def display(dummy1):
    res = []
    while dummy1:
        res.append(str(dummy1.data))
        dummy1 = dummy1.next
    return ' -> '.join(res)


def main():
    ll = LinkedList()
    ll.insert_multiple([6, 7, 8, 9, 5, 2, 1, 3, 4])
    print(ll)
    print(display(partition(ll, 6)))


if __name__ == "__main__":
    main()


