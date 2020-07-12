# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?

n = 3


def rotate_matrix(matrix):
    for x in range(0, int(n / 2)):
        for y in range(x, n - x - 1):
            # store top row to temp
            temp = matrix[x][y]

            # move left column to top row
            matrix[x][y] = matrix[n - 1 - y][x]

            # move bottom row to left column
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]

            # move right column to bottom row
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]

            # move top row to right column
            matrix[y][n - 1 - x] = temp


def display_matrix(matrix):
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=' ')
        print("")


def main():
    # matrix = [[0 for x in range(n)] for y in range(n)]

    matrix = [[1, 2, 3],
              [5, 6, 7],
              [9, 10, 11]]

    rotate_matrix(matrix)
    display_matrix(matrix)


if __name__ == "__main__":
    main()
