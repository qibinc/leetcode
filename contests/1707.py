from typing import List

class BinNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Solution:
    def findmax(self, node, x):
        ans = 0
        for i in range(30, -1, -1):
            if x & (1 << i):
                if node.left:
                    ans += 1 << i
                    node = node.left
                else:
                    node = node.right
            else:
                if node.right:
                    ans += 1 << i
                    node = node.right
                else:
                    node = node.left
        return ans

    def insertNode(self, node, x):
        for i in range(30, -1, -1):
            if x & (1 << i):
                if node.right is None:
                    node.right = BinNode()
                node = node.right
            else:
                if node.left is None:
                    node.left = BinNode()
                node = node.left

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        queries = [[*x, i] for i, x in enumerate(queries)]
        queries.sort(key=lambda x: x[1])
        ans = [0] * len(queries)
        nums.sort()
        root = BinNode()
        i = 0
        for x, maxv, idx in queries:
            while i < len(nums) and nums[i] <= maxv:
                self.insertNode(root, nums[i])
                i += 1
            ans[idx] = self.findmax(root, x) if i > 0 else -1
        return ans

a = Solution()

print(a.maximizeXor([0,1,2,3,4], [[3,1],[1,3],[5,6]]))
print(a.maximizeXor([5,2,4,6,6,3], [[12,4],[8,1],[6,3]]))