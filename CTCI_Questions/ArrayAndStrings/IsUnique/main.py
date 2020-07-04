"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
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
        if left[i] != right[j]:
            s[k] = left[i]
            i += 1
        else:
            s[k] = right[j]
            j += 1
        k +=1

    while i < len(left):
        s[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        s[k] = right[k]
        j += 1
        k += 1
    return s


def is_unique(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


def main():
    print(is_unique("hello world"))
    print(is_unique("my bad o"))


if __name__ == "__main__":
    main()
