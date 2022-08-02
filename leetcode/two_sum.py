from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for idx, num in enumerate(nums):
            diff = target-num
            if diff not in sums:
                sums[num] = idx
            else:
                return [sums[diff], idx]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in sums:
                sums[num] = i
            else:
                print(sums)
                return [sums[n], i]


input_list = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(input_list, target))
