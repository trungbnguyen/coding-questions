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
    if 0 < n <= 2:
        return 1
    elif n < 1:
        return 0

    f = []
    f[0] = 1
    f[1] = 2