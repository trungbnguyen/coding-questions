# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
# so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, next=None):
        self.head = head
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


# Create 2 pointers: 1 moves 2 steps at a time, 1 moves 1 step at a time
# If there is a loop, the 2 nodes will eventually meet at the same node
def get_start_loop_node(node):
    slow = node
    fast = node

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return slow.data
    return None


def main():
    ll = LinkedList()
    ll.insert_multiple([1, 2, 3, 4])
    print(ll)
    ll.head.next.next.next.next = ll.head.next.next
    print(get_start_loop_node(ll.head))


if __name__ == "__main__":
    main()
