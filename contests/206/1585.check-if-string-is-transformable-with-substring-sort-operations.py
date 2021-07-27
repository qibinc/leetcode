from collections import defaultdict


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        cnts = self.cnt(s)
        cntt = self.cnt(t)
        for pair in cntt:
            if cntt[pair] > cnts[pair]:
                return False
        return True

    def cnt(self, s):
        l2rs = [[0] * 10 for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(10):
                l2rs[i][j] = l2rs[i - 1][j]
            l2rs[i][int(s[i])] += 1
        ans = defaultdict(int)
        for i in range(1, len(s)):
            for j in range(int(s[i]) + 1, 10):
                ans[j, int(s[i])] += l2rs[i - 1][j]
        return ans
