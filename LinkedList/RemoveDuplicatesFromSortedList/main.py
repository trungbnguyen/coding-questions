"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
    Input: 1->1->2
    Output: 1->2

Example 2:
    Input: 1->1->2->3->3
    Output: 1->2->3
"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node


def remove_duplicates(head):
    head = Node()
    first = head
    second = head.next_node if head else None

    while second:
        if first.data == second.data:
            second = second.next_node
            first.next_node = second
        else:
            first = second
            second = second.next_node
    return head


def main():
    print(remove_duplicates([1, 1, 2, 3, 5, 5, 7, 9, 9]))


if __name__ == "__main__":
    main()
