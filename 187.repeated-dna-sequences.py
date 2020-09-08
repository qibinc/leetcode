#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        p = 10
        d = defaultdict(int)
        while p <= len(s):
            d[s[p - 10 : p]] += 1
            p += 1
        return [k for k in d if d[k] > 1]


# @lc code=end

