from typing import List


class Solution:
    def __init__(self):
        self.max = 0

    def maxProduct(self, s: str) -> int:
        self.max = 0
        assigned = [0] * len(s)
        self.recursive_max_product(0, s, assigned, 0, 0)
        return self.max

    def check_and_update(self, s: str, assigned: List[int]):
        s1 = [s[idx] for idx, i in enumerate(assigned) if i == 1]
        s2 = [s[idx] for idx, i in enumerate(assigned) if i == 2]
        if s1 == s1[::-1] and s2 == s2[::-1]:
            self.max = max(self.max, len(s1) * len(s2))

    def recursive_max_product(
        self, idx: int, s: str, assigned: List[int], l1: int, l2: int
    ):
        if ((l1 + l2 + len(s) - idx) / 2) ** 2 < self.max:
            return
        if idx == len(s):
            self.check_and_update(s, assigned)
            return
        for i in range(3):
            assigned[idx] = i
            self.recursive_max_product(
                idx + 1, s, assigned, l1 + (i == 1), l2 + (i == 2)
            )


a = Solution()
print(a.maxProduct("leetcodecom"))
print(a.maxProduct("bb"))
print(a.maxProduct("accbcaxxcxx"))
print(a.maxProduct("aaaaaaaaaaaa"))
print(a.maxProduct("yqqrqqy"))
