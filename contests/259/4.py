class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        nxt = [{}]
        for idx, ch in reversed(list(enumerate(s))):
            d = nxt[-1].copy()
            d[ch] = idx
            nxt.append(d)
        nxt = nxt[::-1][1:]

        def vaildate(substr: str):
            i, j = 0, 0
            t = 0
            while i < len(s):
                if s[i] != substr[j]:
                    i = nxt[i].get(substr[j], len(s))
                if i == len(s):
                    return False
                j += 1
                if j == len(substr):
                    j = 0
                    t += 1
                    if t == k:
                        return True
                i = nxt[i].get(substr[j], len(s))
            return False

        cand = [""]
        ans = ""
        while True:
            new_cand = []
            for x in cand:
                for i in range(26):
                    ch = chr(i + ord('a'))
                    if vaildate(x + ch):
                        new_cand.append(x + ch)
            if len(new_cand) > 0:
                ans = max(new_cand)
            else:
                break
            cand = new_cand
            print(cand)
        return ans

a = Solution()
print(a.longestSubsequenceRepeatedK("letsleetcode", 2))
print(a.longestSubsequenceRepeatedK("abcdefgabcdefgh" * 1000, 2000))
