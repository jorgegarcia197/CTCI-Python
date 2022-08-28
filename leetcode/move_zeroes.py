from typing import List 
class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p2] != 0:
                nums[i], nums[p2] = nums[p2], nums[i]
                i += 1
            p2 += 1
        
        return nums
                 






if __name__ == "__main__":
    nums =[0,1,0,3,12]
    print(Solution().moveZeroes2(nums))
        