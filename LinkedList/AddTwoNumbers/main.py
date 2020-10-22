# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
from random import randint


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, data=None, next=None):
        self.head = head
        self.data = data
        self.next = next

    def __str__(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.val))
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
        for _ in range(0, 10):
            self.insert_tail(randint(0, 9))

    def insert_multiple(self, data):
        for v in data:
            self.insert_tail(v)


def add_two_numbers(l1, l2):
    carry = 0
    head = n = Node(0)

    while l1 or l2 or carry:
        if l1:
            val1 = l1.val
            l1 = l1.next
        else:
            val1 = 0

        if l2:
            val2 = l2.val
            l2 = l2.next
        else:
            val2 = 0

        carry, val = divmod(val1 + val2 + carry, 10)
        n.next = n = Node(val)

    return head.next


def main():
    ll1 = LinkedList()
    ll1.insert_multiple([1, 2, 3])

    ll2 = LinkedList()
    ll2.insert_multiple([4, 5, 4])

    print(ll1)
    print(ll2)

    total = add_two_numbers(ll1, ll2)
    print(total)


if __name__ == "__main__":
    main()




