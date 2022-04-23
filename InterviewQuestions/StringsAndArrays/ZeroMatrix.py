matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def nullify_row(matrix, row, num_columns):
    for col in range(num_columns):
        matrix[row][col] = 0


def nullify_column(matrix, column, num_rows):
    for row in range(num_rows):
        matrix[row][column] = 0


def Zero_matrix(matrix):
    locations = []
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    # First we check for all the zeroes in the matrix so we can grab their locations
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                locations.append((row, col))

    # Now that we have the locations of all the zeroes, we can nullify its rows and columns one by one
    for location in locations:
        # Helper function to nullify the row, we pass in the row, the number of columns in the matrix
        nullify_row(matrix, location[0], num_columns)
        # Helper function to nullify the column, we pass in the column, the number of rows in the matrix
        nullify_column(matrix, location[1], num_rows)
    return matrix


if __name__ == '__main__':
    print(Zero_matrix(matrix))
