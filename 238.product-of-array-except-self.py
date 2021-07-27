#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
        suffix = [1]
        for i in range(len(nums) - 1, 0, -1):
            suffix.append(suffix[-1] * nums[i])
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[len(nums) - i - 1])
        return ans


# @lc code=end
