#
# @lc app=leetcode id=2712 lang=python3
#
# [2712] Minimum Cost to Make All Characters Equal
#

# @lc code=start
class Solution:
    def minimumCost(self, s: str) -> int:
        return min(
            self.flipToZero(s),
            self.flipToZero(s.replace("0", "2").replace("1", "0").replace("2", "1")),
        )

    def flipToZero(self, s) -> int:
        mid = len(s) // 2
        return self.flipRightToLeft(s[:mid]) + self.flipRightToLeft(s[mid:][::-1])

    def flipRightToLeft(self, s) -> int:
        ret = 0
        reverse = 0
        for idx in reversed(range(len(s))):
            if int(s[idx]) ^ reverse == 1:
                reverse ^= 1
                ret += idx + 1
        return ret


# @lc code=end

a = Solution()
print(a.minimumCost("0011"))
print(a.minimumCost("010101"))
