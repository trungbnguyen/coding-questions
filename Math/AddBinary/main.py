"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"
"""


def add_binary(a, b):
    binary_sum = bin(int(a, 2) + int(b, 2))
    return binary_sum[2:]


def main():
    print(add_binary("11", "1"))


if __name__ == "__main__":
    main()
