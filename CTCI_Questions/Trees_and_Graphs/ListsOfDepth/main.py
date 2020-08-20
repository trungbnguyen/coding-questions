# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
import collections


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def binary_tree_to_lists(root):
    ret = []
    if not root:
        return ret
    queue = collections.deque()
    queue.appendleft(root)
    while queue:
        size = len(queue)
        dummy = Node(0)
        curr = dummy
        for i in range(size):
            tnode = queue.pop()
            curr.next = Node(tnode.val)
            curr = curr.next
            if tnode.left:
                queue.appendleft(tnode.left)
            if tnode.right:
                queue.appendleft(tnode.right)
        ret.append(dummy.next)
    return ' -> '.join(str(ret))


def main():
    tree = TreeNode(1)
    some_sub_trees = {"left": TreeNode(2), "right": TreeNode(3)}
    some_sub_trees["left"].left = TreeNode(4)
    some_sub_trees["left"].right = TreeNode(5)
    some_sub_trees["right"].left = TreeNode(6)
    some_sub_trees["right"].right = TreeNode(7)
    some_sub_trees["right"].right.right = TreeNode(8)
    some_sub_trees["left"].left.left = TreeNode(9)
    tree.left = some_sub_trees["left"]
    tree.right = some_sub_trees["right"]
    ttll = binary_tree_to_lists(tree)
    print(ttll)


if __name__ == "__main__":
    main()
