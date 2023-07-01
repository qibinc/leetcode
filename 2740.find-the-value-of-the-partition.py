#
# @lc app=leetcode id=2740 lang=python3
#
# [2740] Find the Value of the Partition
#

# @lc code=start
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        ret = 10 ** 9
        nums = sorted(nums)
        for idx in range(len(nums) - 1):
            if abs(nums[idx + 1] - nums[idx]) < ret:
                ret = abs(nums[idx + 1] - nums[idx])
        return ret

# @lc code=end

