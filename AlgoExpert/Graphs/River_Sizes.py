directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def get_neighbors(matrix, row, col, visited):
    neighbors = []
    for direction in directions:
        newRow = row + direction[0]
        newCol = col + direction[1]
        if newRow < 0 or newRow >= len(matrix) or newCol < 0 or newCol >= len(matrix[0]) or visited[newRow][newCol]:
            continue
        neighbors.append((newRow, newCol))
    return neighbors


def riverSizes(matrix):
    output = []
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    for rows in range(len(matrix)):
        for columns in range(len(matrix[0])):
            if matrix[rows][columns] == 1:
                print("Started at: ", rows, columns)
                counter = 0
                stack = [(rows, columns)]
                while len(stack) > 0:
                    currentRow, currentColumn = stack.pop()
                    if visited[currentRow][currentColumn]:
                        continue
                    counter += 1
                    matrix[currentRow][currentColumn] = 2
                    visited[currentRow][currentColumn] = True
                    neighbors = get_neighbors(
                        matrix, currentRow, currentColumn, visited)
                    for neighbor in neighbors:
                        row, col = neighbor
                        if matrix[row][col] == 1 and not visited[row][col]:
                            stack.append((row, col))

                output.append(counter)
    return sorted(output)


if __name__ == "__main__":
    matrix = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    print(riverSizes(matrix))
