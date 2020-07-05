"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has
sufficient space at the end to hold the additional characters, and that you are given the "true" length
of the string. (Note: If implementing in Java, please use a character array so that you can perform this
operation in place.)

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""


def urlify(st, true_length):
    return st[:true_length].replace(' ', '%20')
    # space_count = 0
    # st = list(st)
    # for i in st:
    #     if i == ' ':
    #         space_count += 1
    # no_of_chars = true_length - space_count
    # index = true_length + space_count * 2 + no_of_chars
    # if true_length < len(st):
    #     st[true_length] = '\0'
    #
    # for i in range(true_length - 1, 0):
    #     if st[i] == ' ':
    #         st[index - 1] = '0'
    #         st[index - 2] = '2'
    #         st[index - 3] = '%'
    #         index -= 3
    #     else:
    #         st[index - 1] = st[i]
    #         index -= 1
    # return st


def main():
    print(urlify("Mr John Smith   ", 13))


if __name__ == "__main__":
    main()
