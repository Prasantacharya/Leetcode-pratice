class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1 , max2 = float("-inf"), float("-inf")
        for item in nums:
            max1 = max(max1 + item, item)
            if max2 < max1:
                max2 = max1
        return max2
        
