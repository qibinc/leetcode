#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.val2node = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        self.cloneGraphRecursive(node)
        return self.val2node[node.val]
    
    def cloneGraphRecursive(self, node):
        if not node.val in self.val2node:
            self.val2node[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            if not neighbor.val in self.val2node:
                self.cloneGraphRecursive(neighbor)
            self.val2node[node.val].neighbors.append(self.val2node[neighbor.val])


# @lc code=end

