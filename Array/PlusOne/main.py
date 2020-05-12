"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
"""


def plus_one(nums):
    num = 0
    i = 0
    while i < len(nums):
        num *= 10
        num += nums[i]
        i += 1
    num += 1
    return [int(j) for j in str(num)]


def main():
    print(plus_one([1, 2, 9]))
    print(plus_one([9]))


if __name__ == "__main__":
    main()
