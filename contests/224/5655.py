from typing import List
from itertools import accumulate

class Solution:

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_sum_col = [] * n
        for j in range(n):
            prefix_sum_col.append([0] + list(accumulate([matrix[i][j] for i in range(m)])))
        if m <= n:
            ans = 0
            for i1 in range(m):
                for i2 in range(m):
                    cnt = 0
                    for j in range(n):
                        if prefix_sum_col[j][i2 + 1] - prefix_sum_col[j][i1] == i2 - i1 + 1:
                            cnt += 1
                    ans = max(ans, cnt * (i2 - i1 + 1))
        else:
            start_end = set()
            ans = 0
            for j in range(n):
                i1, i2, cnt = 0, 0, 0
                while i1 < m:
                    while i1 < m and matrix[i1][j] == 0:
                        i1 += 1
                    if i1 == m: continue
                    i2 = i1
                    while i2 < m and matrix[i2][j] == 1:
                        i2 += 1
                    start_end.add((i1, i2))
                    i1 = i2
            start_end = list(start_end)
            start_end.sort(key=lambda x: x[1])
            for idx, (start, end) in enumerate(start_end):
                for j in reversed(range(idx + 1)):
                    if start_end[j][1] < start:
                        break
                    i1, i2 = start, start_end[j][1]
                    cnt = 0
                    for k in range(n):
                        if prefix_sum_col[k][i2] - prefix_sum_col[k][i1] == i2 - i1:
                            cnt += 1
                    ans = max(ans, cnt * (i2 - i1))
        return ans

a = Solution()
print(a.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
