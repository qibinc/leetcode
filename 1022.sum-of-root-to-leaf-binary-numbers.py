#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.sumRootToLeafRecursive(root, 0)

    def sumRootToLeafRecursive(self, root: TreeNode, val: int) -> int:
        if root.left is None and root.right is None:
            return (val << 1) + root.val
        ret = 0
        if root.left is not None:
            ret += self.sumRootToLeafRecursive(root.left, root.val + (val << 1))
        if root.right is not None:
            ret += self.sumRootToLeafRecursive(root.right, root.val + (val << 1))
        return ret


# @lc code=end
