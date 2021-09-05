# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node.left and not node.right:
                # at a leaf node
                return (node.val, node.val)
            if node.left and node.right:
                # path returns path, maximum is the max under that path
                # path can always be taken, maximum may be closed off
                (path1, max1) = dfs(node.left)
                (path2, max2) = dfs(node.right)
                return (max(path1, path2, 0) + node.val , max(max1, max2, path1 + path2 + node.val, path1 + node.val, path2 + node.val, node.val))
            if node.left:
                (path1, max1) = dfs(node.left)
                return (max(path1, 0) + node.val , max(max1, path1 + node.val, node.val))
            if node.right:
                (path2, max2) = dfs(node.right)
                return (max(path2, 0) + node.val, max(max2, path2 + node.val, node.val))
        
        result = dfs(root)
        return max(result[0], result[1])
