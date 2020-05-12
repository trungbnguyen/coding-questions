"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1
"""


def search_insert_position(nums, target):
    """
    User binary search to search for the potential position to insert target if it's not already in the list
    :type nums: list
    :type target: int
    :return: the position of the target or its potential position in the list
    """

    if target in nums:
        return nums.index(target)
    else:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


def main():
    print(search_insert_position([1, 2, 3, 4], 4))
    print(search_insert_position([1, 3, 5, 6], 2))
    print(search_insert_position([1, 3, 5, 6], 7))


if __name__ == "__main__":
    main()



