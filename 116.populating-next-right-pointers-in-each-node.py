#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # def connect(self, root: 'Node') -> 'Node':
    #     ret = self._connect(root)
    #     ans = []
    #     for x in reversed(ret):
    #         ans += x + ['#']
    #     return ans

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        # left_ret = self.connect(root.left)
        # right_ret = self.connect(root.right)
        if root.left:
            root.left.next = root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

# @lc code=end

