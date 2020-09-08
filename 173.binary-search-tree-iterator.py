#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path = [root] if root else []
        self.left = [False]
        self.right = [False]

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ret = None
        while ret is None:
            last = self.path[-1]
            print(last.val)
            if last.left and not self.left[-1]:
                self.left[-1] = True
                self.path.append(last.left)
                self.left.append(False)
                self.right.append(False)
                last = last.left
            else:
                if not last.right:
                    ret = last.val
                    self.path.pop()
                    self.left.pop()
                    self.right.pop()
                elif not self.right[-1]:
                    ret = last.val
                    self.right[-1] = True
                    self.path.append(last.right)
                    self.left.append(False)
                    self.right.append(False)
                else:
                    self.path.pop()
                    self.left.pop()
                    self.right.pop()
        return ret

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        while self.path:
            if self.right[-1]:
                self.path.pop()
                self.left.pop()
                self.right.pop()
            else:
                break
        return bool(self.path)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

