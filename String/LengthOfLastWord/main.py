"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
    Input: "Hello World"
    Output: 5

Solution: use the .split() function as it will get rid of all of spaces
"""


def len_last_word(s):
    # new_s = s.split(' ')
    # last_word_len = 0
    # for i in range(0, len(new_s)):
    #     if new_s[i] == '':
    #         i += 1
    #     else:
    #         last_word_len = len(new_s[i])
    # return last_word_len
    s1 = s.split()
    return len(s1[-1])


def main():
    print(len_last_word("Hello World"))
    print(len_last_word("b   a    "))
    print(len_last_word("a "))


if __name__ == "__main__":
    main()
