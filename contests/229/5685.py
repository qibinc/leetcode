class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        ans = ""
        for c1, c2 in zip(word1[:l], word2[:l]):
            ans += c1 + c2
        ans += word1[l:] + word2[l:]
        return ans

a = Solution()
print(a.mergeAlternately("ab", "pqrs"))