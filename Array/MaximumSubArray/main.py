"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
    which is more subtle.
"""


def max_subarray(nums):
    """
    Iterate through the array and sum up the 2 continuous number if the previous number is greater than 0
    Keep doing this until the end, and return the largest value of the final array
    :type: list
    :rtype:int
    """
    if not nums:
        return 0

    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def main():
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()

