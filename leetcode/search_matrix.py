from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # Basically if it exist within that row
            if target >= row[0] and target <= row[-1]:
                # Do binary search
                return self.binarySearch(row, target)

        return False

    def binarySearch(self,list, target):
        left = 0
        right = len(list)-1

        while left <= right:
            mid = (left+right)//2
            if target == list[mid]:
                return True
            elif target < list[mid]:
                right = mid-1
            elif target > list[mid]:
                left = left+1
        return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(Solution().searchMatrix(matrix, target))
