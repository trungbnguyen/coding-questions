"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
"""


def longest_common_prefix(s_list):
    """
    Create an iterator of the input list
    i
    :param s_list: input list
    :return: the longest common prefix
    """
    result = []
    # using asterisk to unpack the strings in the list into tuples
    # use zip to pair these strings together to compare
    zipped = zip(*s_list)
    for i in zipped:
        if len(set(i)) == 1:
            result.append(i[0])
        else:
            break

    return ''.join(result)


def main():
    print(longest_common_prefix(["flower", "flow", "flight"]))


if __name__ == "__main__":
    main()

