class Solution:
    def modifyString(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i] != '?':
                ans += s[i]
                continue
            for c in ['a', 'b', 'c']:
                if i > 0 and ans[i - 1] == c:
                    continue
                if i < len(s) - 1 and s[i + 1] == c:
                    continue
                break
            ans += c
        return ans

