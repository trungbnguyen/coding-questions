# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.
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


def sum_list(n1, n2):
    ll = LinkedList()
    carry = 0

    while n1.head or n2.head:
        result = carry
        if n1.head:
            result += n1.head.data
            n1.head = n1.head.next
        if n2.head:
            result += n2.head.data
            n2.head = n2.head.next

        ll.insert_tail(result % 10)
        carry = result // 10

    if carry:
        ll.insert_tail(carry)
    return ll


def ll_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count


def sum_list_follow_up(ll1, ll2):
    dummy1, dummy2 = ll1.head, ll2.head
    len1, len2 = ll_length(dummy1), ll_length(dummy2)

    if len1 > len2:
        for _ in range(len1 - len2):
            ll2.insert_head(0)
    elif len2 > len1:
        for _ in range(len2 - len1):
            ll1.insert_head(0)

    n1, n2 = ll1.head, ll2.head
    result = 0

    while n1 and n2:
        result = (result * 10) + n1.data + n2.data
        n1 = n1.next
        n2 = n2.next

    ll = LinkedList()
    ll.insert_multiple([int(i) for i in str(result)])

    return ll


def main():
    num1 = LinkedList()
    num1.insert_multiple([6, 9, 9])
    num2 = LinkedList()
    num2.insert_multiple([3, 0, 2])
    print(num1)
    print(num2)
    print(sum_list(num1, num2))
    num1.insert_multiple([6, 9, 9])
    num2.insert_multiple([3, 0, 2])
    print(sum_list_follow_up(num1, num2))


if __name__ == "__main__":
    main()
