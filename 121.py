class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            # print(f"{prices[right]} - {prices[left]}")
            if prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
            elif prices[right] < prices[left]:
                left = right
            right += 1
        return profit
