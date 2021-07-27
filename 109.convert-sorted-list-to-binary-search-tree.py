#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        pointer = head
        length = 0
        while pointer is not None:
            length += 1
            pointer = pointer.next
        _, root = self.construct_bst(head, 0, length)
        return root

    def construct_bst(self, head, start, end):
        if start == end:
            return head, None
        mid = (start + end) >> 1
        head, left = self.construct_bst(head, start, mid)
        val = head.val
        head = head.next
        head, right = self.construct_bst(head, mid + 1, end)
        return head, TreeNode(val, left, right)


# @lc code=end
