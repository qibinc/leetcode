#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.mem = [True] * (len(s) + 1)
        return self.wordBreakRecursive(s, wordDict)

    def wordBreakRecursive(self, s: str, wordDict: List[str]) -> bool:
        if not self.mem[len(s)]:
            return False
        if s == "":
            return True
        for w in wordDict:
            if len(w) > len(s): continue
            if s[:len(w)] == w and self.wordBreakRecursive(s[len(w):], wordDict):
                return True
        self.mem[len(s)] = False
        return False

# @lc code=end

