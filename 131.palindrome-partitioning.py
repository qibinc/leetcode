#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return [[]]
        if len(s) == 1:
            return [[s]]
        result = []
        for i in range(1, len(s) + 1):
            if s[len(s) - i :] == s[len(s) - i :][::-1]:
                ret = self.partition(s[: len(s) - i])
                for x in ret:
                    x.append(s[len(s) - i :])
                    result.append(x)
        return result


# @lc code=end
