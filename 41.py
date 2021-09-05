class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # smallest has to be from 0 - len(nums)
        lookup = [True] * len(nums)
        for number in nums:
            if number > 0 and number <= len(lookup):
                lookup[number - 1] = False
            
        for i in range(len(lookup)):
            if lookup[i]:
                return i + 1
        return len(nums) + 1
