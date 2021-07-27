#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret = self._pathSum(root, sum)
        return [reversed(x) for x in ret]

    def _pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []

        left_ret = self._pathSum(root.left, sum - root.val)
        for x in left_ret:
            x.append(root.val)
        right_ret = self._pathSum(root.right, sum - root.val)
        for x in right_ret:
            x.append(root.val)
        return left_ret + right_ret


# @lc code=end
