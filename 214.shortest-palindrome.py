#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:

    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        q = s + s[::-1]
        f = [0] * len(q)
        for i in range(1, len(q)):
            t = f[i - 1]
            while t > 0 and (q[t] != q[i] or q[t] == q[i] and t + 1 > len(s)):
                t = f[t - 1]
            if q[t] == q[i]:
                t += 1
            f[i] = t
        length = max(len(s) - f[len(q) - 1], 0)
        return s[::-1][:length] + s
        
# @lc code=end

a = Solution()
print(a.shortestPalindrome("aacecaaa"))
print(a.shortestPalindrome("abcd"))
print(a.shortestPalindrome("aaaa"))
print(a.shortestPalindrome("aabba"))
