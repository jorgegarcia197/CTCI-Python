from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left <= right:
            total = numbers[left]+numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    nums = [5, 25, 75]
    target = 100
    print(Solution().twoSum(nums, target))
