#
# @lc app=leetcode id=2679 lang=python3
#
# [2679] Sum in a Matrix
#

from typing import List

# @lc code=start
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for i in range(len(nums)):
            nums[i] = sorted(nums[i], reverse=True)
        ret = 0
        for j in range(len(nums[0])):
            ret += max(nums[i][j] for i in range(len(nums)))
        return ret


# @lc code=end

a = Solution()
print(a.matrixSum([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
print(a.matrixSum([[1]]))
