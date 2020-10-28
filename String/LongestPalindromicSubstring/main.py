# Given a string s, return the longest palindromic substring in s
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Solution: starting from the middle of the string;
# expand left and right; keep track of the longest palindrome substring

def longest_palindromic_substring(s):
    if not s or s == "":
        return 0

    if len(s) < 2:
        return s

    start = end = 0

    for i in range(0, len(s)):
        len1 = expand_from_middle(s, i, i)  # odd number of characters
        len2 = expand_from_middle(s, i, i + 1)  # even number of character
        len3 = max(len1, len2)

        if len3 > end - start:
            start = i - ((len3 - 1) // 2)
            end = i + (len3 // 2)

    return s[start:end + 1]


def expand_from_middle(s, left, right):
    if not s or left > right:
        return 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def main():
    s = "babad"
    print(longest_palindromic_substring(s))

    s = "racecar"
    print(longest_palindromic_substring(s))

    s = "cbbd"
    print(longest_palindromic_substring(s))


if __name__ == "__main__":
    main()
