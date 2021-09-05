# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        queue = [root]
        output = []
        # checks if there is a tree
        if not root:
            return output
        # bfs, go until queue is empty
        while len(queue):
            tempQueue = []
            temp = []
            for item in queue:
                temp.append(item.val)
                if item.left:
                    tempQueue.append(item.left)
                if item.right:
                    tempQueue.append(item.right)
            output.append(temp)
            queue = tempQueue
        # return the number of iterations
        return output
