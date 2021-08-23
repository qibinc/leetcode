#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        list_s = list(s)
        j = len(s) - 1
        ans = 0
        num_left = 0
        for i in range(len(list_s)):
            if list_s[i] == "[":
                num_left += 1
            else:
                if num_left == 0:
                    # swap once
                    while list_s[j] != "[":
                        j -= 1
                    list_s[i], list_s[j] = list_s[j], list_s[i]
                    j -= 1
                    ans += 1
                    num_left += 1
                else:
                    num_left -= 1
        return ans


# @lc code=end
a = Solution()
print(a.minSwaps("][]["))
print(a.minSwaps("]]][[["))
print(a.minSwaps("[]"))
print(a.minSwaps("]["))
