#
# @lc app=leetcode id=2611 lang=python3
#
# [2611] Mice and Cheese
#

from typing import List

# @lc code=start
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        arr = sorted(map(lambda tup: (tup[0] - tup[1], tup[0], tup[1]), zip(reward1, reward2)), reverse=True)
        return sum(map(lambda tup: tup[1], arr[:k])) + sum(map(lambda tup: tup[2], arr[k:]))


# @lc code=end

a = Solution()
print(a.miceAndCheese([1,1,3,4], [4,4,1,1], 2))
print(a.miceAndCheese([1,1], [1,1], 2))
