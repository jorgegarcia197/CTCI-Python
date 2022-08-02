from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num**2 for num in nums]
        output = []

        left = 0
        right = len(nums)-1

        while left <= right:
            max_value = max(nums[left], nums[right])
            output.insert(0, max_value)
            if max_value == nums[left]:
                left += 1
            else:
                right -= 1
        return output


if __name__ == "__main__":
    input_list = [-5, -3, -2, -1]
    print(Solution().sortedSquares(input_list))
