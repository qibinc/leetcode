#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

from typing import List


# @lc code=start

ZERO = 50


class Solution:
    def getXSmallest(self, counter: List[int], x: int) -> int:
        t = 0
        for i in range(-50, 0):
            t += counter[i + ZERO]
            if t >= x:
                return i
        return 0

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = [0] * 101
        for i in range(k):
            counter[nums[i] + ZERO] += 1
        ret = []
        for i in range(k, len(nums)):
            ret.append(self.getXSmallest(counter, x))
            counter[nums[i - k] + ZERO] -= 1
            counter[nums[i] + ZERO] += 1
        ret.append(self.getXSmallest(counter, x))
        return ret


# @lc code=end

a = Solution()
print(a.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2))
print(a.getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2))
print(a.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1))
