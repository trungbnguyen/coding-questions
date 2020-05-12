"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

    Given nums = [3,2,2,3], val = 3,

    Your function should return length = 2, with the first two elements of nums being 2.

    It doesn't matter what you leave beyond the returned length.
"""


def remove_element(nums, val):
    if not nums:
        return 0

    i = 0
    total = len(nums)
    while i < total:
        if nums[i] == val:
            nums.pop(i)
            total -= 1
        else:
            i += 1

    return len(nums)


def main():
    print(remove_element([3, 2, 2, 3], 3))
    print(remove_element([0,1,2,2,3,0,4,2], 2))


if __name__ == "__main__":
    main()
