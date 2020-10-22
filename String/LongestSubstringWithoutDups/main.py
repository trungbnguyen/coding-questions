# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0


def longest_substring_wo_dups_length(s):
    if not s or s == "":
        return 0

    my_set = set()
    count = 0
    i = 0
    j = 0

    while j < len(s):
        if s[j] not in my_set:
            my_set.add(s[j])
            j += 1
            count = max(len(my_set), count)
        else:
            my_set.discard(s[i])
            i += 1
    return count


def main():
    s1 = "abcabcbb"
    s2 = "bbbb"
    s3 = ""
    s4 = "pwwkew"

    print(longest_substring_wo_dups_length(s1))
    print(longest_substring_wo_dups_length(s2))
    print(longest_substring_wo_dups_length(s3))
    print(longest_substring_wo_dups_length(s4))


if __name__ == "__main__":
    main()
