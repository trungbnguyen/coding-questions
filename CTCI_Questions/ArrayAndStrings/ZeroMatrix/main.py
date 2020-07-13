# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


def zero_matrix(matrix):
    zero_rows = [i for i, row in enumerate(matrix) if not all(row)]
    zero_cols = [i for i, col in enumerate(zip(*matrix)) if not all(col)]

    number_of_cols = len(matrix[0])
    for rowi in zero_rows:
        matrix[rowi] = [0] * number_of_cols

    for coli in zero_cols:
        for row in matrix:
            row[coli] = 0


def display_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")


def main():
    matrix = [[5, 3, 2, 1],
              [-3, 0, 5, 0],
              [0, -1, 2, 6]]

    zero_matrix(matrix)
    display_matrix(matrix)


if __name__ == "__main__":
    main()
