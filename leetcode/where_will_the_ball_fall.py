from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        rows, columns = len(grid), len(grid[0])

        def dfs(row, column):
            if row == rows-1:
                return column
            #! Check if the ball is left-wall stuck:
            if column == 0 and grid[row][column] == -1:
                return -1
            #! Check if the ball is right-wall stuck:
            if column == columns - 1 and grid[row][column] == 1:
                return -1
            #! Check if a ball is stuck in a V shape path:
            if grid[row][column] == 1 and grid[row][column+1] == -1 or grid[row][column] == -1 and grid[row][column-1] == 1:
                return -1
            # ! Continue to search the next row:
            return dfs(row+1, column + grid[row][column])

        for i in range(columns):
            res.append(dfs(0, i))
        return res


if __name__ == "__main__":
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1]]
    print(Solution().findBall(grid))
