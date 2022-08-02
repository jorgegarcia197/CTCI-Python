from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left= 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                max_profit = max(max_profit,profit)
            else:
                left =right
            right +=1
        return max_profit


"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
