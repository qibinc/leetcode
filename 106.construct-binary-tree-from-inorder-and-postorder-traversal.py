#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = postorder[-1]
        root_inorder_idx = inorder.index(root)
        left_inorder = inorder[:root_inorder_idx]
        right_inorder = inorder[root_inorder_idx + 1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]
        node = TreeNode(root, self.buildTree(left_inorder, left_postorder), self.buildTree(right_inorder, right_postorder))
        return node
        
# @lc code=end
