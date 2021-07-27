#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#
from typing import List

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i < j:
            if people[j] + people[i] > limit:
                # people j take a boat itself
                ans += 1
                j -= 1
            else:
                # i and j together
                ans += 1
                i += 1
                j -= 1
        if i == j:
            ans += 1
        return ans


# @lc code=end

a = Solution()
print(a.numRescueBoats([1, 2], 3))
print(a.numRescueBoats([3, 2, 2, 1], 3))
print(a.numRescueBoats([3, 5, 3, 4], 5))
