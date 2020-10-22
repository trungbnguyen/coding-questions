# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
# the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_sumpath(root, sum):
    if root is None:
        return []
    visited, stack = [], [root]
    while stack:
        node = stack.pop()
        visited.append(node)
        stack.extend(filter(None, [node.right, node.left]))
        # append right first, so left will be popped first
        if 

    return visited