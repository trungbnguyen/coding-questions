"""
Given a sorted array nums, remove the duplicates in-place such that each element appear
only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input
array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the returned length.
"""


def remove_duplicates(nums):
    """
    Create a temp variable with value 0
    Iterate through the array and compare element at index i with element at index temp. If the 2 elements are different
    then increase temp, else, replace the element at index temp with element with index i.
    Doing this will create a sub-array of unique numbers for the first temp + 1 elements of the array
    :param nums: the input array
    :return: the length of the sub-array where the items are all unique
    """
    if not nums:
        return 0

    new_tail = 0

    for i in range(0, len(nums)):
        if nums[i] != nums[new_tail]:
            new_tail += 1
        nums[new_tail] = nums[i]
    return new_tail + 1


def main():
    print(remove_duplicates([1, 1, 2]))
    print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))


if __name__ == "__main__":
    main()
