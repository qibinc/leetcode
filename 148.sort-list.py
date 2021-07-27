#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        head = self.sortList(head)
        slow = self.sortList(slow)
        pre_head = ListNode(0, head)
        cur = pre_head
        while cur.next is not None and slow is not None:
            if slow.val <= cur.next.val:
                nxt = slow.next
                self.insert(cur, slow)
                slow = nxt
            cur = cur.next
        if slow is not None:
            cur.next = slow
        return pre_head.next

    def insert(self, prev, v):
        nxt = prev.next
        prev.next = v
        v.next = nxt


# @lc code=end
