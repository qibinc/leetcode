#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

from typing import List

# @lc code=start
class Solution:
    def satisfy(self, piles, h, k):
        ans = 0
        for pile in piles:
            ans += (pile + k - 1) // k
        return ans <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while r - l > 0:
            mid = (l + r) >> 1
            if self.satisfy(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

a = Solution()
print(a.minEatingSpeed([3, 6, 7, 11], 8))
print(a.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(a.minEatingSpeed([30, 11, 23, 4, 20], 6))
