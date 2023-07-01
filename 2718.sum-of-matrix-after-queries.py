#
# @lc app=leetcode id=2718 lang=python3
#
# [2718] Sum of Matrix After Queries
#

# @lc code=start
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        uniq_queries = []
        appeared = set()
        for tp, idx, val in reversed(queries):
            if (tp, idx) in appeared:
                continue
            uniq_queries.append((tp, idx, val))
            appeared.add((tp, idx))
        queries = list(reversed(uniq_queries))
        ret, row_sum, col_sum = 0, 0, 0
        
        for tp, idx, val in queries:
            if tp == 0:
                ret += n * val - col_sum
                row_sum += val
            else:
                ret += n * val - row_sum
                col_sum += val
        return ret
        
# @lc code=end

