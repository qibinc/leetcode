#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        pre_head = ListNode(0, head)
        tail = head
        while tail.next is not None:
            if tail.next.val >= tail.val:
                tail = tail.next
                continue
            v = self.delete(tail, tail.next)
            prev, cur = pre_head, pre_head.next
            while cur is not None and v.val > cur.val:
                prev = prev.next
                cur = cur.next
            self.insert(prev, v)
            if tail.next == v:
                tail = tail.next
        return pre_head.next

    def delete(self, prev, cur):
        prev.next = cur.next
        return cur

    def insert(self, prev, cur):
        nxt = prev.next
        prev.next = cur
        cur.next = nxt


# @lc code=end
