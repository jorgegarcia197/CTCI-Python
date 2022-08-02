from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        number_of_items = len(mat)*len(mat[0])
        if number_of_items != r*c:
            # invalid matrix
            return mat
        output = [[0 for _ in range(c)] for _ in range(r)]
        tmp = []
        for row in range(mat):
            for column in range(mat[0]):
                tmp.append(mat[row][column])
        
        k = 0 
        for row in range(r):
            for col in range(c):
                output[row][col] = tmp[k]
                k += 1
        return output

    def matrixReshape_2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        number_of_items = len(mat)*len(mat[0])
        if number_of_items != r*c:
            # invalid matrix
            return mat
        output = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for row in range(r):
            for col in range(c):
                output[k//c][k%c] = mat[row][col]
                k+=1
        return output
                
        