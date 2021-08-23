from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n_negative = sum([sum([x <= 0 for x in line]) for line in matrix])
        if n_negative % 2 == 0:
            return sum([sum([abs(x) for x in line]) for line in matrix])
        else:
            return (
                sum([sum([abs(x) for x in line]) for line in matrix])
                - min([abs(x) for line in matrix for x in line]) * 2
            )


a = Solution()
print(a.maxMatrixSum([[1, -1], [-1, 1]]))
print(a.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
print(a.maxMatrixSum([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]))
print(a.maxMatrixSum([[2, 9, 3], [5, 4, -4], [1, 7, 1]]))
