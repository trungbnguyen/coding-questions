# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character
# is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
# [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1)
# or INT_MIN (−231) is returned.
# Example:
# Input: str = "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-',
# which is the minus sign. Then take as many numerical digits as possible, which gets 42.
# Example:
# Input: str = "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w',
# which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.

def string_to_integer(s):
    if not s or s == "":
        return 0

    for i in range(len(s)):
        if s[i] == ' ':
            i += 1
        else:
            break

    new_s = s[i:]
    res = 0
    sign = ['-', '+']

    if not new_s or new_s == "":
        return 0

    if new_s[0] not in sign:
        for i in range(len(new_s)):
            if new_s[i].isdigit():
                res = res * 10 + int(new_s[i])
            else:
                break

    else:
        for i in range(1, len(new_s)):
            if new_s[i].isdigit():
                res = res * 10 + int(new_s[i])
            else:
                break

    if new_s[0] == '-':
        if -res > (-2) ** 31:
            return -res
        else:
            return (-2) ** 31

    else:
        if res < (2 ** 31) - 1:
            return res
        else:
            return (2 ** 31) - 1


def main():
    s = "42"
    print(string_to_integer(s))
    s = "   -42"
    print(string_to_integer(s))
    s = "4193 with words"
    print(string_to_integer(s))
    s = " "
    print(string_to_integer(s))
    s = "  +0 123"
    print(string_to_integer(s))
    s = " words and 987"
    print(string_to_integer(s))
    s = "-91283472332"
    print(string_to_integer(s))


if __name__ == "__main__":
    main()
