class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dpTable = [amount + 1] * (amount + 1) # trying to get the minimum, this is an impossible max
        dpTable[0] = 0 # 0 is always possible
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dpTable[i] = min(1 + dpTable[i - coin], dpTable[i]) # choose the smaller of the two
        return dpTable[amount] if dpTable[amount] < amount + 1 else -1 
