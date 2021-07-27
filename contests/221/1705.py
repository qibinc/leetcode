import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        to_rot = []
        ans = 0
        for i in range(n):
            if apples[i] > 0:
                heapq.heappush(to_rot, (i + days[i], apples[i]))
            while to_rot:
                d, app = heapq.heappop(to_rot)
                if i < d:
                    ans += 1
                    if app - 1 > 0:
                        heapq.heappush(to_rot, (d, app - 1))
                    break
        i += 1
        while to_rot:
            d, app = heapq.heappop(to_rot)
            if i < d:
                i += 1
                ans += 1
                if app - 1 > 0:
                    heapq.heappush(to_rot, (d, app - 1))
        return ans


a = Solution()
print(a.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
print(a.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]))
