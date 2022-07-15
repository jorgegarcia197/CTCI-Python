from hashlib import new
from inspect import stack
from sklearn import neighbors


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def get_neighbors(matrix, row, col):
    neighbors = []
    for direction in directions:
        newRow = row + direction[0]
        newCol = col + direction[1]
        if newRow < 0 or newRow >= len(matrix) or newCol < 0 or newCol >= len(matrix[0]):
            continue
        neighbors.append((newRow, newCol))
    return neighbors


def minimum_passes(matrix):
    passes = 0
    visited = [[False for _ in range(len(matrix[0]))]
               for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] < 0:
                passes += 1
                print("Starting at: ", row, column)
                counter = 0
                stack = [(row, column)]
                while len(stack) > 0:
                    currentRow, currentColumn = stack.pop()
                    counter += 1
                    matrix[currentRow][currentColumn] = matrix[currentRow][currentColumn] * -1
                    visited[currentRow][currentColumn] = True

                    neighbors = get_neighbors(
                        matrix, currentRow, currentColumn, visited)
                    for neighbor in neighbors:
                        row, col = neighbor
                        if matrix[row][col] > 0 and not visited[row][col]:
                            stack.append((row, col))
        return passes


def minimum_passes_3(matrix):
    passes = 0
    visited = [[False for _ in range(len(matrix[0]))]
               for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] > 0:
                passes += 1
                print("Starting at: ", row, column)
                stack = [(row, column)]
                while len(stack) > 0:
                    currentRow, currentColumn = stack.pop()
                    neighbors = get_neighbors(
                        matrix, currentRow, currentColumn, visited)
                    for neighbor in neighbors:
                        row, col = neighbor
                        if matrix[row][col] < 0 and not visited[row][col]:
                            matrix[row][row] = matrix[row][row] * -1
                            visited[row][col] = True
                            stack.append((row, col))
    return passes


def containsNeg(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] < 0:
                return True
    return False


def getAllPositives(matrix):
    stack = []
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] > 0:
                stack.append((row, column))
    return stack


def minimum_passes_2(matrix):
    passes = 0
    stack = getAllPositives(matrix)

    while len(stack) > 0:
        initial_length = len(stack)
        passes += 1
        second_stack = []
        counter = 0
        while counter < initial_length:
            currentRow, currentColumn = stack.pop()

            neighbors = get_neighbors(
                matrix, currentRow, currentColumn)
            for neighbor in neighbors:
                row, col = neighbor
                if matrix[row][col] < 0:
                    matrix[row][col] = matrix[row][col] * -1

                    second_stack.append((row, col))
            counter += 1
        stack = second_stack
    return passes - 1 if not containsNeg(matrix) else -1


if __name__ == "__main__":
    input_matrix = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1]
    ]
    print(minimum_passes_2(input_matrix))
