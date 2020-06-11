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


def main():
    print(is_symmetric([1, 2, 2, 3, 4, 4, 3]))


if __name__ == "__main__":
    main()
