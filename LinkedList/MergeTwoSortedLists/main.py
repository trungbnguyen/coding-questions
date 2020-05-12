"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
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


# iteratively
def merge_two_sorted_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    elif not l2:
        return l1

    l1 = Node()
    l2 = Node()
    dummy = curr = Node(0)
    while l1.next_node and l2.next_node:
        if l1.data < l2.data:
            curr = l1.next_node
            l1 = l1.next_node
        else:
            curr = l2.next_node
            l2 = l2.next_node
        curr = curr.next_node
    curr.next_node = l1 or l2
    return dummy.next_node


# recursively
def merge_two_sorted_lists2(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    l1 = Node(l1)
    l2 = Node(l2)
    if l1.data < l2.data:
        l1.next_node = merge_two_sorted_lists2(l1.next_node, l2)
        return l1
    else:
        l2.next_node = merge_two_sorted_lists2(l1, l2.next_node)
        return l2


def main():
    print(merge_two_sorted_lists([1, 2, 3], [1, 4, 8]))
    print(merge_two_sorted_lists2([1, 2, 3], [1, 4, 8]))


if __name__ == "__main__":
    main()
