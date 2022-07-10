import math


def searchInSortedMatrix(matrix, target):
    # Write your code here.
    for i in range(len(matrix)):
        row = matrix[i]
        found, idx = BinarySearch(row, target)
        if found:
            return[i, idx]

    return [-1, -1]


def BinarySearch(array, target):
    if len(array) <= 0:
        return False, -1
    left = 0
    right = len(array)-1

    return BShelper(array, target, left, right)


def BShelper(array, target, left, right):
    if left > right:
        return False,-1
    middle = math.floor((left+right)/2)
    if target == array[middle]:
        return True, middle
    elif target < array[middle]:
        right = middle-1
        return BShelper(array, target, left, right)
    elif target > array[middle]:
        left = middle+1
        return BShelper(array, target, left, right)
    
def searchInSortedMatrix2(matrix, target):
    # Write your code here.
    row, column = 0, len(matrix[0])-1
    while row >= 0 and row <= len(matrix) and column >= 0 and column <= len(matrix[0]):
        if matrix[row][column] < target:
            row +=1
        elif matrix[row][column] > target:
            column -= 1
        else:
            return [row,column]
    return [-1,-1]



if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    target = 44
    print(searchInSortedMatrix2(matrix, target))
