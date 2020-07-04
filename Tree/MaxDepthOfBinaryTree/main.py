"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

      3
     / \
    9  20
    /  \
   15   7

Return its depth = 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = None
        self.right = None
        self.val = val


def tree_max_depth(self, root):
    def traverse(left, right):
        if not root:
            return 0
        count = 0
