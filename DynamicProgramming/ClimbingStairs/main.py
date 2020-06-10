"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
"""


def climbing_stairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    ways_to_one_step_before = 2
    ways_to_two_step_before = 1
    all_ways = 0

    for i in range(2, n):
        all_ways = ways_to_one_step_before + ways_to_two_step_before
        ways_to_two_step_before = ways_to_one_step_before
        ways_to_one_step_before = all_ways

    return all_ways


def main():
    print(climbing_stairs(10))


if __name__ == "__main__":
    main()

