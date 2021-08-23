#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

from typing import List

# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])


# @lc code=end


a = Solution()
print(a.numOfStrings(["a", "b", "c"], "aaaaabbbbb"))
