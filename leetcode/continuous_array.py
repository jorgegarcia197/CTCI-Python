from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        max_ending_idx = 0 
        for i in range(len(nums)):
            max_ending_idx += nums[i]
            max_so_far = max(max_so_far,max_ending_idx)
            if max_ending_idx < 0:
                max_ending_idx = 0
        return max_so_far
