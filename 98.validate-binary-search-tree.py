#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        valid, maxn, minn = self._isValidBST(root)
        return valid

    def _isValidBST(self, root: TreeNode) -> (bool, int, int):
        if root is None:
            return True, -float("inf"), float("inf")
        minn = root.val

        def val(node):
            if node is not None:
                return node.val
            else:
                return -1

        if root.left is not None:
            valid, submaxn, subminn = self._isValidBST(root.left)
            if not valid or submaxn >= root.val:
                return False, None, None
            minn = min(minn, subminn)
        maxn = root.val
        if root.right is not None:
            valid, submaxn, subminn = self._isValidBST(root.right)
            if not valid or subminn <= root.val:
                return False, None, None
            maxn = max(maxn, submaxn)
        return True, maxn, minn


# @lc code=end
