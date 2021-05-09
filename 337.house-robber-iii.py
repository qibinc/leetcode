#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Tuple, Union

class Solution:
    def _rob(self, root: Union[TreeNode, None]) -> Tuple[int, int]:
        if root is None:
            return 0, 0
        left_r, left_nor = self._rob(root.left)
        right_r, right_nor = self._rob(root.right)
        return root.val + left_nor + right_nor, max(left_nor, left_r) + max(right_nor, right_r)

    def rob(self, root: TreeNode) -> int:
        return max(*self._rob(root))
# @lc code=end

a = Solution()
print(a.rob(TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))))
print(a.rob(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))))
