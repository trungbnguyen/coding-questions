"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Solution:
    One-pass HashTable: While we iterate and inserting elements into the table,
    we also look back to check if current element's complement already exists in the table.
    If it exists, we have found a solution and return immediately.
"""


def two_sum(nums, target):
    """
    Create a HashTable. Iterate and inserting element into this table.
    Check if current element's complement already exist in table.
    If it exists, we have found a solution and return immediately.
    :param nums: list of integers
    :param target: target sum
    :return: list of indices of 2 integers that sum up target
    """
    d = {}

    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in d:
            return [d[complement], i]

        d[nums[i]] = i


def main():
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 7, 11, 15], 18))
    print(two_sum([2, 7, 11, 15], 13))
    print(two_sum([3, 2, 4], 7))
    print(two_sum([3, 2, 4], 5))
    print(two_sum([3, 2, 4], 6))


if __name__ == "__main__":
    main()
