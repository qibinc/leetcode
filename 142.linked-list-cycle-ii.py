#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        nxt = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            nxt = True
            if fast == slow:
                break
        if fast != slow or not nxt:
            return None
        last = head
        while last != slow:
            last = last.next
            slow = slow.next
        return last

# @lc code=end
