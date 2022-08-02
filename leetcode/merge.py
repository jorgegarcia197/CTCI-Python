from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        return nums1.sort()


nums1 = [0]
m= 0
nums2=[1]
n= 1
print(Solution().merge(nums1, m, nums2, n))
