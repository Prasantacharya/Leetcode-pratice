"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = [node]
        head = Node(node.val)
        itr = head
        lookup = {node.val: head}
        while len(queue) > 0:
            itr = lookup[queue[0].val]
            for neighbor in queue[0].neighbors:
                if neighbor.val not in lookup:
                    lookup[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                itr.neighbors.append(lookup[neighbor.val])
            queue.pop(0)
        return head
        
