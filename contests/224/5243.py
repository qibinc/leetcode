from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        results = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                results[nums[i] * nums[j]] += 1
        ans = 0
        for _, times in results.items():
            ans += times * (times - 1) * 4
        print(results)
        return ans

a = Solution()
print(a.tupleSameProduct([2,3,4,6]))