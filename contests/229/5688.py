class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # ans1 = self.longestCommonSubsequence(word1, word2[::-1])
        # ans2 = self.longestCommonSubsequence(word1[:-1], word2[::-1])
        # ans3 = self.longestCommonSubsequence(word1, word2[1:][::-1])
        # ans = max(ans1 * 2, ans2 * 2 + 1, ans3 * 2 + 1)
        # return ans if ans > 0 else 0
        word = word1 + word2
        return max(self.longestCommonSubsequence(word, word[::-1], len(word2)), 0)

    def longestCommonSubsequence(self, word1: str, word2: str, k: int):
        n, m = len(word1), len(word2)
        l = n - k
        word1 = "$" + word1
        word2 = "$" + word2
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i + j > n:
                    continue
                if j <= k or j > k and f[i][j - 1] > 0:
                    f[i][j] = max(f[i][j], f[i][j - 1])
                if i <= l or i > l and f[i - 1][j] > 0:
                    f[i][j] = max(f[i - 1][j], f[i][j])
                if (i <= l or i > l and f[i - 1][j] > 0) and (
                    j <= k or j > k and f[i - 1][j - 1] > 0
                ):
                    if word1[i] == word2[j]:
                        f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        ans = float("-inf")
        for i in range(1, n + 1):
            if f[i][n - i] > 0:
                ans = max(ans, f[i][n - i] * 2)
        for i in range(1, n + 1):
            if f[i - 1][n - i] > 0:
                ans = max(ans, f[i - 1][n - i] * 2 + 1)
        return ans


a = Solution()
print(a.longestPalindrome("cacb", "cbba"))
print(a.longestPalindrome("ab", "ab"))
print(a.longestPalindrome("aa", "bb"))
print(a.longestPalindrome("aa", "aa"))
print(a.longestPalindrome("a", "b"))
print(a.longestPalindrome("afaaadacb", "ca"))
