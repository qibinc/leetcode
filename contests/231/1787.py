from typing import List
from collections import Counter


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        counters = [Counter() for _ in range(len(nums))]
        for i in range(k):
            for j in range(i, len(nums), k):
                counters[i][nums[j]] += 1
        s = 0
        xor = 0
        for i in range(k):
            print(counters[i])
            s += (
                (len(nums) // k)
                + (i < len(nums) % k)
                - counters[i].most_common(1)[0][1]
            )
            xor ^= counters[i].most_common(1)[0][0]
        f = [[-10000] * 1024 for _ in range(k + 1)]
        f[0][0] = 0
        prev_max = 0
        for i in range(k):
            m = 0
            for j in range(1024):
                f[i + 1][j] = prev_max
                for num, cnt in counters[i].items():
                    f[i + 1][j] = max(f[i][j ^ num] + cnt, f[i + 1][j])
                m = max(m, f[i + 1][j])
            prev_max = max(prev_max, m)
        return len(nums) - f[k][0]


a = Solution()
print(a.minChanges([1, 2, 4, 1, 2, 5, 1, 2, 6], 3))
print(a.minChanges([1, 2, 0, 3, 0], 1))
print(a.minChanges([3, 4, 5, 2, 1, 7, 3, 4, 7], 3))
print(a.minChanges([1, 2, 4, 1, 2, 5, 1, 2, 6], 3))
print(a.minChanges([26, 19, 19, 28, 13, 14, 6, 25, 28, 19, 0, 15, 25, 11], 3))
