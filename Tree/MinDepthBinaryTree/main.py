# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if not root:
        return 0
    elif root.left and root.right:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    else:
        return 1 + max(min_depth(root.left), min_depth(root.right))


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(min_depth(root))

    root = TreeNode(1)
    root.left = TreeNode(2)

    print(min_depth(root))


if __name__ == "__main__":
    main()
