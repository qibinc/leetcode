#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        ans = []
        if root is not None:
            q.append((root, 0))
        last_level = -1
        while q:
            node, level = q.popleft()
            if level != last_level:
                ans.append(deque())
                last_level = level
            if level % 2 == 0:
                ans[-1].append(node.val)
            else:
                ans[-1].appendleft(node.val)
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
        return ans


# @lc code=end
