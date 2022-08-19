from typing import List
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        source_color = image[sr][sc]
        stack = [(sr,sc)]
        while stack:
            current = stack.pop()
            currentRow,currentCol  = current
            image[currentRow][currentCol] == color
            neighbors = self.get_neighbors(image,currentRow,currentCol)
            for neighbor in neighbors:
                next_row,next_col = neighbor
                if image[next_row][next_col] == source_color:
                    stack.append((sr,sc))
        return image 
            
    def floodFill_2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        if image[sr][sc] == color:
            return image
        starting_pixel =  image[sr][sc]
        queue = [(sr,sc)]
        while queue:
            current = queue.pop(0)
            row, col = current
            image[row][col] = color
            neighbors = self.get_neighbors(image, row, col)
            for neighbor in neighbors:
                if image[neighbor[0]][neighbor[1]] == starting_pixel:
                    queue.append(neighbor)
        return image
            
            
            
    def get_neighbors(self,matrix, row, col):
        neighbors = []
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]
            if newRow < 0 or newRow >= len(matrix) or newCol < 0 or newCol >= len(matrix[0]):
                continue
            neighbors.append((newRow, newCol))
        return neighbors
            