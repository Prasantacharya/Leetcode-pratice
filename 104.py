# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        queue = [root]
        height = 0
        if not root:
            return 0
        while len(queue):
            tempQueue = []
            for item in queue:
                if item.left:
                    tempQueue.append(item.left)
                if item.right:
                    tempQueue.append(item.right)
            height += 1
            queue = tempQueue
        return height
