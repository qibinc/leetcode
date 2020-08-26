#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None, None
        left, right = root.left, root.right
        lhead, ltail = self.flatten(left)
        rhead, rtail = self.flatten(right)
        root.left = None
        if lhead is None:
            root.right = rhead
        else:
            root.right = lhead
            ltail.right = rhead
        if rhead:
            tail = rtail
        else:
            if lhead:
                tail = ltail
            else:
                tail = root
        return root, tail
# @lc code=end

