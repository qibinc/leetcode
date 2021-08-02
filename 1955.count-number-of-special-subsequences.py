from typing import List

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        f0, f1, f2 = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        f0[0] = int(nums[0] == 0)
        for i, num in list(enumerate(nums))[1:]:
            f0[i] = f0[i - 1] + (f0[i - 1] + 1 if num == 0 else 0)
            f1[i] = f1[i - 1] + (f0[i - 1] + f1[i - 1] if num == 1 else 0)
            f2[i] = f2[i - 1] + (f2[i - 1] + f1[i - 1] if num == 2 else 0)
        return f2[-1] % (10 ** 9 + 7)
        
a = Solution()
print(a.countSpecialSubsequences([0,1,2,2]))
print(a.countSpecialSubsequences([2,2,0,0]))
print(a.countSpecialSubsequences([0,1,2,0,1,2]))
