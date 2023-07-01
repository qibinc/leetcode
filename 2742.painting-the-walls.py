#
# @lc app=leetcode id=2742 lang=python3
#
# [2742] Painting the Walls
#

from typing import List

# @lc code=start
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        m = n * 2 + 1
        MAX = 10 ** 6 * 500
        dp = [[MAX] * (m + 1) for _ in range(n + 1)]
        dp[0][n] = 0
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j < m:
                    dp[i][j] = dp[i - 1][j + 1]
                if j - time[i - 1] >= 0 and dp[i - 1][j - time[i - 1]] + cost[i - 1] < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - time[i - 1]] + cost[i - 1]
        for row in dp:
            print(row)
        return min(dp[n][n:])

# @lc code=end

a = Solution()
print(a.paintWalls(
    [2, 2],
    [5, 5]
))
