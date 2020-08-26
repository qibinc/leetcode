#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
    def connect(self, root: 'Node') -> 'Node':
        prev = tail = None
        node = root
        
        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                prev = node.left
                if not(tail):
                    tail = prev
                
            if node.right:
                if prev:
                    prev.next = node.right
                prev = node.right
                if not(tail):
                    tail = prev
                
            node = node.next
            if not node:
                node = tail
                prev = tail = None
                
        return root

# class Solution:

#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return None
#         if root.left:
#             if root.right:
#                 root.left.next = root.right
#             elif root.next:
#                 if root.next.left:
#                     root.left.next = root.next.left
#                 else:
#                     root.left.next = root.next.right
#         if root.right:
#             t = root.next
#             while t:
#                 if t.left:
#                     root.right.next = t.left
#                     break
#                 elif t.right:
#                     root.right.next = t.right
#                     break
#                 else:
#                     t = t.next
#         self.connect(root.left)
#         self.connect(root.right)
#         return root
        
# @lc code=end

