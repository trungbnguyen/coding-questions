#  Given two (singly) linked lists, determine if the two lists intersect.
#  Return the intersecting node. Note that the intersection is defined based on reference, not value.
#  That is, if the kth node of the first linked list is the exact same node (by reference)
#  as the jth node of the second linked list, then they are intersecting.


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


def get_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count


def find_intersection(node1, node2):
    if node1 is None or node2 is None:
        return None

    len1, len2 = get_length(node1), get_length(node2)
    diff = abs(len1 - len2)

    shorter_list_node = node1 if len1 < len2 else node2
    longer_list_node = node2 if len1 < len2 else node1

    # Match starting point for traversal of the 2 lists
    for _ in range(diff):
        longer_list_node = longer_list_node.next

    while shorter_list_node.next != longer_list_node.next:
        shorter_list_node = shorter_list_node.next
        longer_list_node = longer_list_node.next

    return longer_list_node


def main():
    ll1 = LinkedList()
    ll1.insert_multiple([6, 2, 3, 7, 73, 9])

    ll2 = LinkedList()
    ll2.insert_multiple([4, 7, 9, 13])

    print(find_intersection(ll1.head, ll2.head).data)


if __name__ == "__main__":
    main()
