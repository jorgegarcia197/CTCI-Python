def rotateMatrix(matrix):
    n = len(matrix)
    for i in range(len(matrix)-1):
        for j in range(i,n): ## This loop is an important detail, that we are just traversing through the values of the matrix we havent rotated yet
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
