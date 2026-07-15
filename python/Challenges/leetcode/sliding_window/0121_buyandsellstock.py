from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l, r = 0, 1
        maxprofit = max(0, prices[r] - prices[l])
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
                r = i
            elif prices[i] > prices[r]:
                r = i
            if prices[r] - prices[l] > maxprofit:
                maxprofit = prices[r] - prices[l]
        return maxprofit


prices = [7, 6, 4, 3, 1]
sol = Solution()
print(sol.maxProfit(prices))  # output: 5
