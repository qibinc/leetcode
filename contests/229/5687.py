from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        nums = [0] + nums
        multipliers = [0] + multipliers
        # f[i][j]: max score for multipliers[1..i] on nums[1..j] and nums[n-i+1+j..n]
        f = [[float('-inf')] * (m + 1) for _ in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            for j in range(i + 1):
                if j > 0:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + multipliers[i] * nums[j])
                if j < i:
                    f[i][j] = max(f[i][j], f[i - 1][j] + multipliers[i] * nums[n - i + 1 + j])
        return max(f[m][j] for j in range(m + 1))

a = Solution()
print(a.maximumScore([1,2,3], [3,2,1]))
print(a.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
print(a.maximumScore([0, 1], [100]))
