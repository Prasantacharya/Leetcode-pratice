# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = [(root, -1)]
        flag = {}
        flag[x] = {"parent": -1, "found":False}
        flag[y] = {"parent": -1, "found": False}
        while len(queue):
            children = []
            for item in queue:
                if item[0].left:
                    children.append((item[0].left, item[0].val))
                if item[0].right:
                    children.append((item[0].right, item[0].val))
                if item[0].val == x or item[0].val == y:
                    flag[item[0].val]["found"] = True
                    flag[item[0].val]["parent"] = item[1]
            if flag[x]["found"] and flag[y]["found"] and flag[x]["parent"] != flag[y]["parent"]:
                return True
            else:
                flag[x] = {"parent": -1, "found":False}
                flag[y] = {"parent": -1, "found":False}
            queue = children
        return False
