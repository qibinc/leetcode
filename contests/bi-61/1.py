from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, x in enumerate(nums):
            for y in nums[idx + 1:]:
                if abs(x - y) == k:
                    ans += 1
        return ans
        