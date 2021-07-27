from collections import defaultdict


class Solution:
    def getMaxPalindromeLength(self, queryStr):
        # write code here
        d = defaultdict(int)
        for ch in queryStr:
            d[ch] += 1
        hasOdd = False
        ans = 0
        for key in d:
            if d[key] % 2 == 1:
                hasOdd = True
            ans += 2 * (d[key] // 2)
        return ans + hasOdd


a = Solution()
print(a.getMaxPalindromeLength("abccccdd"))
