import numpy as np
from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        count = np.zeros((len(nums) + 1, 101))
        for idx, num in enumerate(nums):
            count[idx + 1] = count[idx]
            count[idx + 1, num] = count[idx, num] + 1
        ans = []
        for l, r in queries:
            last_k = -1
            min_diff = 100
            for k in range(1, 101):
                if count[r + 1, k] - count[l, k] > 0:
                    if last_k != -1 and k - last_k < min_diff:
                        min_diff = k - last_k
                    last_k = k
            if min_diff == 100:
                min_diff = -1
            ans.append(min_diff)
        return ans

a = Solution()
print(a.minDifference([1,3,4,8], [[0,1],[1,2],[2,3],[0,3]]))
print(a.minDifference([4,5,2,2,7,10], [[2,3],[0,2],[0,5],[3,5]]))