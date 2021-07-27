#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if len(bin(m)) != len(bin(n)):
            return 0
        ans = 0
        for i in range(2, len(bin(m))):
            ans *= 2
            if bin(m)[i] != bin(n)[i]:
                break
            ans += int(bin(m)[i])
        return ans * 2 ** (len(bin(m)) - i - 1)


# @lc code=end
