"""
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows.
"""


def reverse_integer(num):
    rev = 0
    original = num
    if original < 0:
        num *= -1
    while num > 0:
        # extract the last digit of the number
        last_digit = num % 10

        # add it to the reverse number
        rev = rev * 10 + last_digit

        # remove the last digit from the number
        num //= 10

    # check for max and min value of the reverse in 32-bit platforms
    if rev <= (-2 ** 31) or rev >= (2 ** 31) - 1:
        return 0
    elif original < 0:
        return -rev
    return rev


def main():
    print(reverse_integer(3214))
    print(reverse_integer(142511669))
    print(reverse_integer(1351313613611541))
    print(reverse_integer(-1351313613611541))
    print(reverse_integer(-15153))
    print(reverse_integer(-7673))
    print(reverse_integer(1441999))


if __name__ == "__main__":
    main()
