#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start

import numpy as np


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        f = np.zeros((len(word1) + 1, len(word2) + 1), dtype=int)
        f[0] = np.arange(len(word2) + 1)
        f[:, 0] = np.arange(len(word1) + 1)
        for i in range(1, 1 + len(word1)):
            for j in range(1, 1 + len(word2)):
                f[i, j] = min(f[i - 1, j], f[i, j - 1], f[i - 1, j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    f[i, j] = min(f[i, j], f[i - 1, j - 1])
        return f[len(word1), len(word2)]


# @lc code=end

a = Solution()
print(a.minDistance("horse", "ros"))
print(a.minDistance("intention", "execution"))
