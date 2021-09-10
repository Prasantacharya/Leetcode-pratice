class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        goal = len(nums) - 1
        index = goal
        while index >= 0:
            if nums[index] + index >= goal:
                # print(f"{nums[index]} + {index} can reach {goal}")
                goal = index
                if index == 0:
                    return True
            index -= 1
        return False
