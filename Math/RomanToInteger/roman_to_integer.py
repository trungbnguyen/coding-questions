"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


def roman_to_int(s):
    """
    A function to convert roman numeral to integer
    :param s: input string represent the roman numerals
    :return: return the integer equivalence
    """
    roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_reverse = s[::-1]
    result = roman_to_int_map[s_reverse[0]]  # set the result to the first value of the string

    # Iterate through the reverse string
    # if the value of the key, whose position is after the current position of i in the reverse string, is SMALLER than
    # the value of the key whose position match that of i in the reverse string, then subtract the value of the former
    # from result. Otherwise, add it to the result
    # Taking advantage of the fact that larger number precedes smaller ones in roman number, whenever a smaller number
    # precede a larger number, subtract the value of that smaller number.
    for i in range(0, len(s_reverse) - 1):
        if roman_to_int_map[s_reverse[i + 1]] < roman_to_int_map[s_reverse[i]]:
            result -= roman_to_int_map[s_reverse[i + 1]]
        else:
            result += roman_to_int_map[s_reverse[i + 1]]

    return result


def main():
    print(roman_to_int("III"))
    print(roman_to_int("IV"))


if __name__ == "__main__":
    main()
