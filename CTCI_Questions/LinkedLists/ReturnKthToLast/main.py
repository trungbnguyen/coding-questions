# Implement an algorithm to find the kth to last element of a singly linked list.
from random import randint


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, size=None):
        self.head = head
        self.size = size

    # Display
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
            prev = curr
            curr = curr.next

    def delete2(self, data):
        if self.head is None:
            return self.head

        curr = self.head
        if curr.data == data:
            self.head = curr.next

        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            else:
                curr = curr.next


def find_kth_to_last(ll, k):
    head = ll.head
    curr = ll.head
    size = 0

    if head is None:
        return head

    while curr:
        curr = curr.next
        size += 1

    if size < k:
        return head
    else:
        kth_to_last = size - k - 1
        curr = ll.head
        for _ in range(kth_to_last):
            curr = curr.next
        return curr.data


def main():
    ll = LinkedList()
    ll.generate()
    print(ll)
    print(find_kth_to_last(ll, 3))


if __name__ == "__main__":
    main()
