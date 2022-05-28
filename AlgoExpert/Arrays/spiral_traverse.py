

def spiral_traverse(matrix):
    sR = 0
    sC = 0
    eR = len(matrix)-1
    eC = len(matrix[0]) - 1
    output = []

    while sR <= eR and sC <= eC:
        # Traverse Top
        for i in range(sC, eC + 1):
            output.append(matrix[sR][i])

        # Traverse Right
        for i in range(sR+1, eR+1):
            output.append(matrix[i][eC])
        # Traverse Bottom
        for i in reversed(range(sC, eC)):
            if sR == eR:
                break
            output.append(matrix[eR][i])

        # Traverse Left
        for i in reversed(range(sR+1, eR)):
            if sC == eC:
                break
            output.append(matrix[i][sC])

        sR += 1
        eR -= 1
        sC += 1
        eC -= 1
    return output


if __name__ == '__main__':
    input_dict = {
        "array": [
            [1, 2, 3],
            [12, 13, 4],
            [11, 14, 5],
            [10, 15, 6],
            [9, 8, 7]
        ]
    }
    print(spiral_traverse(input_dict["array"]))
