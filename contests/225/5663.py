from collections import defaultdict
from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        smatrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        mamm = 0
        for i in range(len(matrix)):
            smatrix[i][0] = matrix[i][0]
            for j in range(1, len(matrix[0])):
                smatrix[i][j] = smatrix[i][j - 1] ^ matrix[i][j]
                mamm = max(mamm, matrix[i][j])
            mamm = max(mamm, matrix[i][0])
        result = defaultdict(int)
        for j in range(len(matrix[0])):
            result[smatrix[0][j]] += 1
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                smatrix[i][j] ^= smatrix[i - 1][j]
                result[smatrix[i][j]] += 1
        rank = 0
        for i in reversed(range(2 * mamm + 1)):
            rank += result[i]
            if rank >= k:
                return i
        
a = Solution()
print(a.kthLargestValue([[5,2],[1,6]], 1))
print(a.kthLargestValue([[5,2],[1,6]], 2))
print(a.kthLargestValue([[5,2],[1,6]], 3))
print(a.kthLargestValue([[5,2],[1,6]], 4))
