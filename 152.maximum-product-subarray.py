#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -float("inf")
        cur_pos = 0
        cur_neg = 0
        for num in nums:
            if num > 0:
                if cur_pos == 0:
                    cur_pos = num
                else:
                    cur_pos *= num
                if cur_neg < 0:
                    cur_neg *= num
                if cur_pos > ans:
                    ans = cur_pos
            elif num < 0:
                old_pos = cur_pos
                cur_pos = cur_neg * num
                if cur_pos > 0 and cur_pos > ans:
                    ans = cur_pos
                cur_neg = old_pos * num
                if cur_neg == 0:
                    cur_neg = num
            else:
                cur_pos = 0
                cur_neg = 0
        if ans == -float("inf"):
            return max(nums)
        return ans


# @lc code=end
