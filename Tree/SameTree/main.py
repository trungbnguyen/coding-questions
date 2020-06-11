"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3

           [1,2,3],   [1,2,3]

Output: true
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def is_same_tree_recursion(self, p, q):
    # Recursion
    if p and q:
        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    else:
        return p is q


def is_same_tree_dfs_stack(self, p, q):
    stack = [(p, q)]
    while stack:
        n1, n2 = stack.pop()
        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        elif not n1 and not n2:
            continue
        else:
            return False
    return True


def main():
    # print(is_same_tree([1, 2, 3], [1, 2, 3]))
    # print(is_same_tree([1, 2], [1, None, 2]))


if __name__ == "__main__":
    main()
