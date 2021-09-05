# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # function to verify if one number matches
        def verify(item,node):
            # check if the value slots where it should
            if (not node):
                return False
            if (node.val == item):
                return True
            # havent found the value yet, keep searching
            if (item > node.val):
                return verify(item, node.right)
            if (item < node.val):
                return verify(item, node.left)
            return False
        
        queue = [root]
        doubleCheck = set()
        while (len(queue) > 0):
            tempQueue = []
            for item in queue:
                if item.val in doubleCheck:
                    return False
                doubleCheck.add(item.val)
                if (verify(item.val, root) == False):
                    return False
                if (item.left):
                    tempQueue.append(item.left)
                if (item.right):
                    tempQueue.append(item.right)
            queue = tempQueue
        return True
