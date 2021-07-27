from typing import List
from itertools import accumulate


class Solution:
    def find_g(self, arr, val, last=0):
        l, r = last, len(arr) - 1
        while l < r:
            m = (l + r) >> 1
            if arr[m] <= val:
                l = m + 1
            else:
                r = m
        if arr[l] > val:
            return l
        else:
            return -1

    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        ans = 0
        last_l, last_r = 0, 0
        for i in range(len(nums) - 2):
            if (prefix_sum[-1] + prefix_sum[i]) / 2 <= 2 * prefix_sum[i] - 1:
                break
            l = self.find_g(prefix_sum, 2 * prefix_sum[i] - 1, max(last_l, i + 1))
            r = self.find_g(
                prefix_sum, (prefix_sum[-1] + prefix_sum[i]) / 2, max(last_r, i + 1)
            )
            if r == -1:
                r = len(nums) - 1
            if l != -1:
                ans += r - l
        return ans % (10 ** 9 + 7)
