from typing import List
from collections import defaultdict


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = defaultdict(int)
        for a, b in rectangles:
            q = gcd(a, b)
            d[(a // q, b // q)] += 1
        ans = 0
        for key in d:
            ans += d[key] * (d[key] - 1) // 2
        return ans


a = Solution()
print(a.interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]))
print(a.interchangeableRectangles([[4, 5], [7, 8]]))
