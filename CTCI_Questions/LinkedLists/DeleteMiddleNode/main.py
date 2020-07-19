# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
# not necessarily the exact middle) of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
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


def delete_mid_node(node):
    node.data = node.next.data
    node.next = node.next.next


def main():
    ll = LinkedList()
    ll.insert_multiple([6, 2, 7, 10, 98, 45, 2])
    print(ll)
    curr = ll.head
    for _ in range(4):
        curr = curr.next
    delete_mid_node(curr)
    print(ll)


if __name__ == "__main__":
    main()
