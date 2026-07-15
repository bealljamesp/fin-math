from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        l, r = 0, 1
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
            if prices[i] > prices[r]:
                r = i
                if prices[r] - prices[l] > maxprofit:
                    maxprofit = prices[r] - prices[l]
        return maxprofit


prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(prices))  # Output: 5
