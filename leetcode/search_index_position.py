from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if target > nums[right]:
            return right+1
        if target in nums:
            return nums.index(target)
        else:
            while left <= right:
                middle = (left+right)//2
                if target == nums[middle]:
                    return middle
                elif target < nums[middle]:
                    right = middle-1
                    continue
                elif target > nums[middle]:
                    left = middle+1
                    continue
            return left


if __name__ == "__main__":
    nums = [1]
    target = 1
    print(Solution().searchInsert(nums, target))
