#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        f = [1] * 1 + [0] * n
        for i in range(1, n + 1):
            for j in range(i):
                f[i] += f[j] * f[i - 1 - j]
        f[0] = 0
        return f[n]


# @lc code=end
