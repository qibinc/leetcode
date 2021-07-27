#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cnt = 0
        cur = head
        if head is None:
            return None
        while cur is not None:
            cnt += 1
            cur = cur.next
        if cnt % 2 == 1:
            mid = head
            c = 0
            while c < (cnt - 1) // 2:
                mid = mid.next
                c += 1
        else:
            mid = head
            c = 0
            while c < cnt // 2 - 1:
                mid = mid.next
                c += 1
            # insert a dummy mid
            v = ListNode()
            v.next = mid.next
            mid.next = v
            mid = v
        prev = mid
        cur = mid.next
        mid.next = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur1, cur2 = head, prev
        while cur1 != cur2:
            nxt1 = cur1.next
            nxt2 = cur2.next
            cur1.next = cur2
            cur2.next = nxt1
            prev = cur2
            cur1, cur2 = nxt1, nxt2
        if cnt % 2 == 0:
            prev.next = None
        return head


# @lc code=end
