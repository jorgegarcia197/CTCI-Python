
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# ! Solution 1


def get_connected_islands(matrix):
    rows, columns = len(matrix), len(matrix[0])
    boolean_matrix = [[False for _ in range(columns)] for _ in range(rows)]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                rowIsBorder = row == 0 or row == rows - 1
                colIsBorder = column == 0 or column == columns - 1
                isBorder = rowIsBorder or colIsBorder
                if not isBorder:
                    continue
                if matrix[row][column] != 1:
                    continue

                findConnected(matrix, row, column, boolean_matrix)

    for row in range(1, len(matrix)-1):
        for column in range(1, len(matrix[row])-1):
            if boolean_matrix[row][column]:
                continue
            matrix[row][column] = 0
    return matrix


def get_neighbors(matrix, row, col):
    neighbors = []
    for direction in directions:
        newRow = row + direction[0]
        newCol = col + direction[1]
        if newRow < 0 or newRow >= len(matrix) or newCol < 0 or newCol >= len(matrix[0]):
            continue
        neighbors.append((newRow, newCol))
    return neighbors


def findConnected(matrix, startRow, startCol, boolean_matrix):
    stack = [(startRow, startCol)]
    while len(stack) > 0:
        currentRow, currentColumn = stack.pop()
        alreadyVisited = boolean_matrix[currentRow][currentColumn]
        if alreadyVisited:
            continue
        boolean_matrix[currentRow][currentColumn] = True
        neighbors = get_neighbors(matrix, currentRow, currentColumn)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] == 1:
                stack.append((row, col))


# ! Solution 2
def findConnectedToTwos(matrix, startRow, startCol):
    stack = [(startRow, startCol)]
    while len(stack) > 0:
        currentRow, currentColumn = stack.pop()
        matrix[currentRow][currentColumn] = 2
        neighbors = get_neighbors(matrix, currentRow, currentColumn)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] == 1:
                stack.append((row, col))


def get_connected_islands_2(matrix):
    rows, columns = len(matrix), len(matrix[0])
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                rowIsBorder = row == 0 or row == rows - 1
                colIsBorder = column == 0 or column == columns - 1
                isBorder = rowIsBorder or colIsBorder
                if not isBorder:
                    continue
                if matrix[row][column] != 1:
                    continue

                findConnectedToTwos(matrix, row, column)

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            value = matrix[row][column]
            if value == 1:
                matrix[row][column] = 0
            elif value == 2:
                matrix[row][column] = 1
    return matrix


if __name__ == "__main__":
    sample_input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
    print(get_connected_islands_2(sample_input))
