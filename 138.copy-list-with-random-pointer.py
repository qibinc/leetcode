#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pre_head = Node(0, head)
        new_pre_head = Node(0)
        cur = pre_head
        new_cur = new_pre_head
        while cur.next:
            new_cur.next = Node(cur.next.val)
            cur = cur.next
            new_cur = new_cur.next
            cur.new = new_cur
        cur, new_cur = pre_head.next, new_pre_head.next
        while cur:
            new_cur.random = cur.random.new if cur.random else None
            cur = cur.next
            new_cur = new_cur.next
        return new_pre_head.next


# @lc code=end

