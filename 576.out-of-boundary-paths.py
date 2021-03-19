#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 10 ** 9 + 7
        f = [[0] * (n + 2) for _ in range(m + 2)]
        f[i + 1][j + 1] = 1
        ans_sum = 0
        for _ in range(N):
            g = [[0] * (n + 2) for _ in range(m + 2)]
            for xi in range(1, m + 1):
                for xj in range(1, n + 1):
                    g[xi - 1][xj] += f[xi][xj]
                    g[xi + 1][xj] += f[xi][xj]
                    g[xi][xj - 1] += f[xi][xj]
                    g[xi][xj + 1] += f[xi][xj]
            f = g
            for xi in range(m + 2):
                ans_sum += f[xi][0] + f[xi][n + 1]
            for xj in range(1, n + 1):
                ans_sum += f[0][xj] + f[m + 1][xj]
        return ans_sum % mod
# @lc code=end

a = Solution()
print(a.findPaths(100, 100, 100, 0, 1))
