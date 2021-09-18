from typing import List
from collections import defaultdict

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        earnings = [0] * (n + 1)
        end_at = defaultdict(list)
        for s, e, t in rides:
            end_at[e].append((s, t))
        for i in range(1, n + 1):
            earnings[i] = earnings[i - 1]
            for s, t in end_at[i]:
                earnings[i] = max(earnings[i], earnings[s] + i - s + t)
        return earnings[n]
