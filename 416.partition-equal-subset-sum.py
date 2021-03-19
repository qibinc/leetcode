#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

from typing import List

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        f = [False] * (s + 1)
        f[0] = True
        for num in nums:
            for x in reversed(range(s + 1)):
                if x >= num:
                    f[x] |= f[x - num]
        return f[s]
        
# @lc code=end

