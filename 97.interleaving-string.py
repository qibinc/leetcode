#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
# import numpy as np
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # f = np.zeros((len(s3) + 2, len(s1) + 1), dtype=bool)
        f = [[False] * (len(s1) + 1) for _ in range(len(s3) + 2)]
        s1 = "^" + s1
        s2 = "^" + s2
        s3 = "^^" + s3
        # f[1, 0] = True
        f[1][0] = True
        for i in range(2, len(s3)):
            for j in range(max(0, i - len(s2)), min(len(s1), i)):
                # f[i, j] = (f[i - 1, j - 1] and s3[i] == s1[j]) or (f[i - 1, j] and s3[i] == s2[i - j - 1])
                f[i][j] = (f[i - 1][j - 1] and s3[i] == s1[j]) or (f[i - 1][j] and s3[i] == s2[i - j - 1])
        return f[len(s3) - 1][len(s1) - 1]
        
# @lc code=end

