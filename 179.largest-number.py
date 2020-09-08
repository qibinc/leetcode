#
# @lc app=leetcode id=179 lang=python2
#
# [179] Largest Number
#


# @lc code=start
class Solution:
    def __init__(self):
        self.root = Node(0)

    def largestNumber(self, nums) -> str:
        def cmp(x, y):
            if x * 10 ** len(str(y)) + y > y * 10 ** len(str(x)) + x:
                return 1
            elif x * 10 ** len(str(y)) + y == y * 10 ** len(str(x)) + x:
                return 0
            else:
                return -1

        sorted(nums, cmp=cmp)
        return "".join(map(str, nums))

a = Solution()
a.largestNumber([3, 30, 34, 5, 9])

# @lc code=end

