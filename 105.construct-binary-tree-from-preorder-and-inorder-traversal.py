#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = preorder[0]
        root_inorder_idx = inorder.index(root)
        left_inorder = inorder[:root_inorder_idx]
        right_inorder = inorder[root_inorder_idx + 1 :]
        left_preorder = preorder[1 : 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder) :]
        node = TreeNode(
            root,
            self.buildTree(left_preorder, left_inorder),
            self.buildTree(right_preorder, right_inorder),
        )
        return node


# @lc code=end
