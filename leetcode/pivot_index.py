from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        totalsum=sum(nums)
        for i in range(len(nums)):
            rightsum=totalsum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            else:
                leftsum+=nums[i]
        return -1

print(Solution().pivotIndex([1,7,3,6,5,6]))