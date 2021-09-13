class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = float("-inf")
        curMax = 1
        curMin = 1
        for number in nums:
            temp = number * curMax
            curMax = max(temp, number * curMin, number)
            curMin = min(temp, number * curMin, number)
            largest = max(curMax, curMin, largest, number)
        return largest 
