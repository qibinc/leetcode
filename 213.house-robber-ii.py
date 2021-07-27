#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

from typing import List

# @lc code=start
class Solution:
    def _rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for m in nums:
            prev_prev, prev = prev, curr
            curr = max(prev, prev_prev + m)
        return curr

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))


# @lc code=end

a = Solution()
print(a.rob([2, 3, 2]))
print(a.rob([2]))
print(a.rob([1, 2, 3, 1]))
print(a.rob([4, 1, 2, 7, 5, 3, 1]))
