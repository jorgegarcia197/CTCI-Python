from collections import defaultdict
from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        diagonals = defaultdict(list)
        
        def save_diagonals(i, j):
            diagonal = []
            while i < rows and j < cols:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            return diagonal

        def build_diagonal(i,j,diag):
            while i < rows and j < cols:
                mat[i][j] = diag.pop()
                i += 1
                j += 1
            
        for j in range(cols):
            key = (0,j)
            diagonals[key] = save_diagonals(0,j)
        for i in range(1,rows):
            key = (i,0)
            diagonals[key] = save_diagonals(i,0)
        
        for indices,diag in diagonals.items():
            i,j = indices
            build_diagonal(i,j,diag)
        return mat
            
