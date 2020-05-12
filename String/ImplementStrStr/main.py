"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
"""


# using KMP
def str_str1(haystack, needle):
    """

    :param needle: the needle to be found
    :param haystack: the haystack environment
    :return: the index of the first occurrence of the needle
    """

    def kmp(a_str):
        j = 0
        prefix = [0]
        for idx in range(1, len(a_str)):
            while j > 0 and a_str[idx] != a_str[j]:
                j = prefix[j - 1]
            if a_str[j] == a_str[idx]:
                j += 1
            else:
                j = 0
            prefix.append(j)
        return prefix

    if not needle or not haystack:
        return 0

    a_string = kmp(needle + '#' + haystack)
    for i in range(len(needle) + 1, len(a_string)):
        if a_string[i] == len(needle):
            return i - 2 * len(needle)

    return -1


# non-KMP solution
def str_str2(haystack, needle):
    """
    Iterate through the substring whose length is the same as needle and check if that substring matches the needle
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle or not haystack:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        # check if the substring 
        if haystack[i:i + len(needle)] == needle:
            return haystack[i:i + len(needle)]
    return -1


def main():
    print(str_str1("hello", "ll"))
    print(str_str2("hello", "lo"))


if __name__ == "__main__":
    main()
