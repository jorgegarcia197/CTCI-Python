from typing import List


def spiral_traverse(matrix: List[List]) -> List:
    starting_row = 0
    ending_row = len(matrix) - 1
    starting_column = 0
    ending_column = len(matrix[0]) - 1
    output = []

    while ending_column >= starting_column and ending_row >= starting_row:
        # Traverse Top
        for i in range(starting_column, ending_column + 1):
            output.append(matrix[starting_row][i])
        # Traverse Right
        for i in range(starting_row+1, ending_row+1):
            output.append(matrix[i][ending_column])
        # Traverse Bottom
        for i in reversed(range(starting_column, ending_column)):
            if starting_row == ending_row:
                break
            output.append(matrix[ending_row][i])
        # Traverse Left
        for i in reversed(range(starting_row+1, ending_row)):
            if starting_column == ending_column:
                break
            output.append(matrix[i][starting_column])
        starting_row += 1
        ending_row -= 1
        starting_column += 1
        ending_column -= 1
    return output


if __name__ == "__main__":
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiral_traverse(input_matrix))
