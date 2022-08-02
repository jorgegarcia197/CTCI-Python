directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
from typing import List
from collections import deque


class Solution:
    fresh_oranges = 0
    def orangesRotting(self, matrix: List[List[int]]) -> int:
        minutes = 0 
        self.fresh_oranges = 0
        queue = deque()
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 1:
                    self.fresh_oranges += 1
                if matrix[row][column] == 2:
                    queue.append((row,column))
        queue_len = len(queue)
        while len(queue) > 0:
            if queue_len == 0:
                queue_len =  len(queue)
                minutes += 1

            current_orange = queue.popleft()
            queue_len -= 1
            row,column = current_orange
            neighbors = self.get_neighbors(row,column,matrix)
            for neighbor in neighbors:
                queue.append(neighbor)
            
        if self.fresh_oranges != 0:
            return -1
        return minutes



    def get_neighbors(self, currentRow, currentColumn, matrix):
        neighbors = []
        for direction in directions:
                newRow = currentRow + direction[0]
                newCol = currentColumn + direction[1]
                if newRow < 0 or newRow >= len(matrix) or newCol < 0 or newCol >= len(matrix[0]):
                    continue
                if matrix[newRow][newCol] == 1:
                    matrix[newRow][newCol] = 2
                    self.fresh_oranges -=1
                    neighbors.append((newRow, newCol))
        return neighbors

if __name__ =="__main__":
    matrix = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(matrix))
        