from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left_start, left_end, right_start, right_end = self.get_pivot_point(
            nums)
        left_result = self.binary_helper(0, left_end, nums, target)
        right_result = self.binary_helper(right_start, right_end, nums, target)

        if left_result != -1:
            return left_result
        elif right_result != -1:
            return right_result
        return -1

    def get_pivot_point(self, nums):
        pivot, last = len(nums)-1, nums[-1]
        while nums[pivot] <= last:
            last = nums[pivot]
            pivot -= 1
        return 0, pivot, pivot+1, len(nums)-1

    def binary_helper(self, left, right, nums, target):
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = left+1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))
