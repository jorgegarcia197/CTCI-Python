from typing import List


class Solution(object):
    def totalImbalance(self, nums):
        total_imbalance = 0
        combinations = self.get_SubArrays(nums, 0, 0, [])
        for comb in combinations:
            if len(comb) <= 1:
                continue
            else:
                comb.sort()
                print(comb)
                if not self.check_continuity(comb):
                    # Basically, if the combination in the list is not continuous, we can safely assure there is an imbalance
                    total_imbalance += 1
        return total_imbalance

    def check_continuity(self, lst):
        for i in range(len(lst)-1):
            if lst[i+1] - lst[i] != 1:
                return False
        return True

    def get_SubArrays(self, arr, start, end, total):
        # Stop if we have reached the end of the array
        if end == len(arr):
            return total
        # Increment the end point and start from 0
        elif start > end:
            return self.get_SubArrays(arr, 0, end + 1, total)

        # Print the subarray and increment the starting point
        else:
            total.append(arr[start:end + 1])
            return self.get_SubArrays(arr, start + 1, end, total)


if __name__ == "__main__":
    input_list = [3,1,2]
    print(Solution().totalImbalance(input_list))
