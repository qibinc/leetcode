#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self._generate(list(range(1, n + 1)))
    
    def _generate(self, nodes):
        if not nodes:
            return [None]
        ans = []
        for root_idx in range(len(nodes)):
            left = self._generate(nodes[:root_idx])
            right = self._generate(nodes[root_idx+1:])
            for l in left:
                for r in right:
                    root = TreeNode(nodes[root_idx])
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans
        
# @lc code=end

