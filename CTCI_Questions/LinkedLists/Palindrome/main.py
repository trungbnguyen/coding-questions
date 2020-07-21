# Implement a function to check if a linked list is a palindrome.
from random import randint


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
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
        for _ in range(0, 10):
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


def copy_list(node):
    new_list = LinkedList()
    while node:
        new_list.insert_tail(node.data)
        node = node.next
    return new_list.head


def reverse_linked_list(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def reverse_linked_list_recursively(head):
    if head is None or head.next is None:
        return head
    # get to the tail of the linked list
    reversed_list_head = reverse_linked_list_recursively(head.next)
    # reverse the pointer between 2 nodes
    head.next.next = head
    head.next = None
    return reversed_list_head


def ll_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count


def ll_is_palindrome(node):
    if not node:
        raise ValueError("Empty list")

    original_list = copy_list(node)
    reversed_list = reverse_linked_list(node)

    if ll_length(original_list) != ll_length(reversed_list):
        return False

    while original_list and reversed_list:
        if original_list.data != reversed_list.data:
            return False
        original_list = original_list.next
        reversed_list = reversed_list.next
    return True


def main():
    ll1 = LinkedList()
    ll1.insert_multiple(['r', 'a', 'c', 'e', 'c', 'a', 'r'])
    print(reverse_linked_list(ll1))
    print(ll_is_palindrome(ll1.head))

    ll2 = LinkedList()
    ll2.insert_multiple([1, 2, 3, 4, 5, 4, 3, 2, 1])
    print(reverse_linked_list(ll2))
    print(ll_is_palindrome(ll2.head))

    # Not palindrome
    ll3 = LinkedList()
    ll3.insert_multiple([1, 2, 3, 4, 5])
    print(reverse_linked_list_recursively(ll3))
    print(ll_is_palindrome(ll3.head))


if __name__ == "__main__":
    main()
