"""
Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.
"""


def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s[k] = left[i]
            i += 1
        else:
            s[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        s[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        s[k] = right[j]
        j += 1
        k += 1
    return s


def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    l1 = list(s1)
    l2 = list(s2)
    a = merge_sort(l1)
    b = merge_sort(l2)

    return a == b


def main():
    print(check_permutation("hello", "elhlo"))
    print(check_permutation("hey", "sup"))


if __name__ == "__main__":
    main()
