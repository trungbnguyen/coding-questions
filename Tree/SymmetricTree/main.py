"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = None
        self.right = None
        self.val = val


def is_symmetric(self, root):
    def is_mirror(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        elif l.val == r.val:
            return is_mirror(l.left, r.right) and is_mirror(l.right, r.left)
        return False

    return is_mirror(root, root)


def is_symmetric_iterative(self, root):
    # Each iteration, it checks whether two nodes are symmetric and then push (node1.left, node2.right),
    # (node1.right, node2.left) to the end of queue.
    if not root:
        return True

    dq = collections.deque([(root.left, root.right)],)
    node1, node2 = dq.popleft()
    while dq:
        if not node1 and not node2:
            continue
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False

        # node1.left and node2.right are symmetric nodes in structure
        # node1.right and node2.left are symmetric nodes in structure
        dq.append((node1.left, node2.right))
        dq.append((node1.right, node2.left))

    return True


def main():
    print(is_symmetric([1, 2, 2, 3, 4, 4, 3]))


if __name__ == "__main__":
    main()
