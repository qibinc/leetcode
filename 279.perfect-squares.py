#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [x * x for x in range(1, 101)]
        f = [n] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for s in perfect_squares:
                if i >= s:
                    f[i] = min(f[i], f[i - s] + 1)
        return f[n]


# @lc code=end

a = Solution()
print(a.numSquares(1))
print(a.numSquares(12))
print(a.numSquares(13))
print(a.numSquares(9999))
print(a.numSquares(10000))
