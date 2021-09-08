#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#


from typing import List
from functools import reduce

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        v = reduce(lambda x, y: x ^ y, nums)
        b = v & (-v)
        ans1, ans2 = 0, 0
        for num in nums:
            if num & b:
                ans1 ^= num
            else:
                ans2 ^= num
        return [ans1, ans2]


# @lc code=end

a = Solution()
print(a.singleNumber([1, 2, 1, 3, 2, 5]))
print(a.singleNumber([-1, 0]))
print(a.singleNumber([0, 1]))
