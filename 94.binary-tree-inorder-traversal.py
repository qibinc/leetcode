#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        ans = []
        parents = []
        while current is not None or parents:
            while current is not None:
                parents.append(current)
                current = current.left
            current = parents.pop()
            ans.append(current.val)
            current = current.right

        return ans
# @lc code=end

