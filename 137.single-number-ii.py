#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        ones, twos = 0, 0
        for x in nums:
            ones = (ones ^ x) & (~twos)
            twos = (twos ^ x) & (~ones)
        return ones
# @lc code=end

