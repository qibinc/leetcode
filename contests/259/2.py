from typing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        suf_min = [nums[-1]]
        for num in reversed(nums[:-1]):
            suf_min.append(min(suf_min[-1], num))
        suf_min = suf_min[::-1]
        pref_max = nums[0]
        ans = 0
        for idx, num in list(enumerate(nums))[1:-1]:
            if pref_max < num and num < suf_min[idx + 1]:
                ans += 2
            elif nums[idx - 1] < num and num < nums[idx + 1]:
                ans += 1
            pref_max = max(pref_max, num)
        return ans
        