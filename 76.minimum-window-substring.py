#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ch_dict = defaultdict(int)
        cnt = 0
        target = Counter(t)
        i, j = 0, 0
        ans = ""
        for j in range(len(s)):
            if s[j] in target:
                ch_dict[s[j]] += 1
                if ch_dict[s[j]] == target[s[j]]:
                    cnt += 1
            if cnt == len(target):
                while i < j and s[i] not in target or ch_dict[s[i]] > target[s[i]]:
                    if s[i] in target:
                        ch_dict[s[i]] -= 1
                    i += 1
            if cnt == len(target) and (not ans or j - i + 1 < len(ans)):
                ans = s[i : j + 1]
        return ans


a = Solution()
print(a.minWindow("ab", "a"))

# @lc code=end
