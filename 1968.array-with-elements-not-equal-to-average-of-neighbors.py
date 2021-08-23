#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

from typing import List

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for idx in range(1, len(nums) - 1):
            if idx % 2 == 1 and (
                nums[idx] < nums[idx - 1] or nums[idx] < nums[idx + 1]
            ):
                a, b, c = sorted([nums[idx - 1], nums[idx], nums[idx + 1]])
                nums[idx - 1], nums[idx], nums[idx + 1] = a, c, b
            elif idx % 2 == 0 and (
                nums[idx] > nums[idx - 1] or nums[idx] > nums[idx + 1]
            ):
                a, b, c = sorted([nums[idx - 1], nums[idx], nums[idx + 1]])
                nums[idx - 1], nums[idx], nums[idx + 1] = c, a, b

        return nums


# @lc code=end

a = Solution()
print(a.rearrangeArray([12, 18, 0, 15, 13, 11]))
print(a.rearrangeArray([0, 12, 8, 14, 9, 13, 17, 15]))
print(a.rearrangeArray([5, 1, 4, 3, 2]))
print(a.rearrangeArray([1, 2, 3]))
print(a.rearrangeArray([1, 2, 3, 4, 5]))
print(a.rearrangeArray([6, 2, 0, 9, 7]))
