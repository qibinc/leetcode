#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# @lc code=end

a = Solution()
print(a.findDuplicate([1, 3, 4, 2, 2]))
print(a.findDuplicate([3, 1, 3, 4, 2]))
print(a.findDuplicate([1, 1]))
print(a.findDuplicate([1, 1, 2]))
