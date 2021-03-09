#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(len(nums)):
            while q and i - q[0][1] >= k:
                q.popleft()
            num = nums[i]
            while q and num >= q[-1][0]:
                q.pop()
            q.append((num, i))
            if i >= k - 1:
                ans.append(q[0][0])
        return ans

        
# @lc code=end

a = Solution()
print(a.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(a.maxSlidingWindow([1], 1))
print(a.maxSlidingWindow([1, -1], 1))
print(a.maxSlidingWindow([9, 11], 2))
print(a.maxSlidingWindow([4, -2], 2))
