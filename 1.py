class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [i, lookup[target - nums[i]]]
            else:
                lookup[nums[i]] = i
        return 0
                
