#
# @lc app=leetcode id=179 lang=python2
#
# [179] Largest Number
#


# @lc code=start
from functools import cmp_to_key


class Solution:
    @staticmethod
    def cmp(num1, num2):
        if int(str(num1) + str(num2)) < int(str(num2) + str(num1)):
            return -1
        elif int(str(num1) + str(num2)) == int(str(num2) + str(num1)):
            return 0
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(Solution.cmp), reverse=True)
        return str(int("".join(map(str, nums))))


a = Solution()
a.largestNumber([3, 30, 34, 5, 9])

# @lc code=end
