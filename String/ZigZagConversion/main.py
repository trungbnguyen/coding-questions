# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

def zigzag_conversion(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s

    direction = -1
    row = 0
    res = [[] for i in range(num_rows)]

    for c in s:
        res[row].append(c)
        if row == 0 or row == num_rows - 1:
            direction *= -1

        row += direction

    for i in range(len(res)):
        res[i] = ''.join(res[i])
    return ''.join(res)


def main():
    s = "PAYPALISHIRING"

    print(zigzag_conversion(s, 3))
    print(zigzag_conversion(s, 4))

    s = "THEPHOENIX"
    print(zigzag_conversion(s, 4))


if __name__ == "__main__":
    main()
