#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.visited = []
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.rightSideViewRecursive(root, 0)
        return self.visited

    def rightSideViewRecursive(self, root, depth):
        if root is None:
            return
        if len(self.visited) <= depth:
            self.visited.append(None)
        self.rightSideViewRecursive(root.right, depth + 1)
        if self.visited[depth] is None:
            self.visited[depth] = root.val
        self.rightSideViewRecursive(root.left, depth + 1)
        
# @lc code=end

