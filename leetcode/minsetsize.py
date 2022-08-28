from collections import Counter
from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = sorted(Counter(arr).values(), reverse=True)
        total_length= len(arr)
        output = 0
        count = 0
        for v in counts:
            count += v
            output +=1
            if count >= total_length/2:
                return output

        return output
if __name__== "__main__":
    arr = [3,3,3,3,5,5,5,2,2,7]
    print(Solution().minSetSize(arr))
        