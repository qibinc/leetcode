from typing import List
from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i, j = 0, 0
        ans = 0
        counter = defaultdict(int)
        current_len = 0
        while j < len(nums):
            while j < len(nums) and nums[j] < nums[i] + len(nums):
                counter[nums[j]] += 1
                if counter[nums[j]] == 1:
                    current_len += 1
                j += 1
            ans = max(current_len, ans)
            counter[nums[i]] -= 1
            if counter[nums[i]] == 0:
                current_len -= 1
            i += 1
        return len(nums) - ans

a = Solution()
print(a.minOperations([4,2,5,3]))
print(a.minOperations([8,5,9,9,8,4]))
