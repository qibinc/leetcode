from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.cnt = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        p_x, p_y = point
        for q_x, q_y in self.cnt:
            if abs(q_x - p_x) == abs(q_y - p_y) and q_x != p_x and q_y != p_y and (q_x, p_y) in self.cnt and (p_x, q_y) in self.cnt:
                # print(q_x, q_y)
                ans += self.cnt[(q_x, q_y)] * self.cnt[(q_x, p_y)] * self.cnt[(p_x, q_y)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

# 1 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 1 0 0
# 1 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 2 0 0 0 1 0 0 1 0 0
# 1 0 0 0 0 0 0 1 0 0
# 1 0 0 0 0 0 0 0 0 1