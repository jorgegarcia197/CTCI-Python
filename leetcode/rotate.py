from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        total_length = len(nums)
        output = [0]*total_length
        for idx, value in enumerate(nums):
            new_index = (idx+k) % total_length
            output[new_index] = value
        return output


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    k = 2
    print(Solution().rotate(nums, k))
