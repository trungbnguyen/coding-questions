# Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    # recursively pass element to left and right subtree
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])
    return root


def preorder(node):
    if not node:
        return None

    print(node.val),
    preorder(node.left)
    preorder(node.right)
    
    
def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = sorted_array_to_bst(arr)
    print("PreOrder Traversal of constructed BST is", preorder(root))


if __name__ == "__main__":
    main()
