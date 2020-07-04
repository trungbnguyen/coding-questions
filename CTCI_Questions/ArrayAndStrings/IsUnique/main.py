"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s):
    s = ''.join(s.split())
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                return False
    return True


def main():
    print(is_unique("hello world"))
    print(is_unique("my bad o"))


if __name__ == "__main__":
    main()
