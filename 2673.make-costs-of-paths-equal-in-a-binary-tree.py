#
# @lc app=leetcode id=2673 lang=python3
#
# [2673] Make Costs of Paths Equal in a Binary Tree
#

from typing import List, Tuple

# @lc code=start
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cost = [0] + cost
        ma, su = self._minIncrements(1, n, cost)
        return su

    def _minIncrements(self, idx, n, cost) -> Tuple[int, int]:
        co = 0
        max_left, sum_left = 0, 0
        max_right, sum_right = 0, 0
        if idx * 2 <= n:
            max_left, sum_left = self._minIncrements(idx * 2, n, cost)
        if idx * 2 + 1 <= n:
            max_right, sum_right = self._minIncrements(idx * 2 + 1, n, cost)

        if max_left > 0 and max_right > 0:
            co = abs(max_left - max_right)
        return cost[idx] + max(max_left, max_right), sum_left + sum_right + co


# @lc code=end

a = Solution()
print(a.minIncrements(7, [1, 5, 2, 2, 3, 3, 1]))
print(a.minIncrements(3, [5, 3, 3]))
