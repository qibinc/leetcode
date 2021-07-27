from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ans = min(self._minCharacters(a, b), self._minCharacters(b, a))
        ans = min(ans, len(a) + len(b) - Counter(a + b).most_common(1)[0][1])
        return ans

    def _minCharacters(self, a: str, b: str) -> int:
        cnta = Counter(a)
        cntb = Counter(b)
        suma, sumb = 0, 0
        ans = len(a) + len(b)
        for idx in range(25):
            ch = chr(ord("a") + idx)
            suma += cnta[ch]
            sumb += cntb[ch]
            ans = min(ans, sumb + len(a) - suma)
        return ans


a = Solution()
# print(a.minCharacters("a", "b"))
print(a.minCharacters("zzzz", "z"))
