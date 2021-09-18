from typing import List
from collections import Counter

MAX = 10 ** 5

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        ans = []
        if counter[0]:
            if counter[0] % 2 == 0:
                ans = [0] * (counter[0] // 2)
            else:
                return []
        for i in range(1, MAX + 1):
            if counter[i] == 0:
                continue
            if counter[i * 2] < counter[i]:
                return []
            counter[i * 2] -= counter[i]
            ans += [i] * counter[i]
        return ans
