from collections import deque
from typing import List


class Solution:
    def visit(self, i, j, grid, visited, group):
        q = deque()
        q.append((i, j))
        visited[i][j] = 1
        groupname = (i, j)
        ret = set([(i, j)])
        while q:
            i, j = q.popleft()
            group[i][j] = groupname
            for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_i, new_j = i + dir[0], j + dir[1]
                if (
                    new_i >= 0
                    and new_j >= 0
                    and new_i < len(grid)
                    and new_j < len(grid[0])
                    and grid[new_i][new_j] == 1
                    and not visited[new_i][new_j]
                ):
                    visited[new_i][new_j] = 1
                    q.append((new_i, new_j))
                    ret.add((new_i, new_j))
        return ret

    def visitall(self, grid):
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        group = [[""] * len(grid[0]) for _ in range(len(grid))]
        d = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not visited[i][j]:
                    d[(i, j)] = self.visit(i, j, grid, visited, group)
        return group, d

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        group1, d1 = self.visitall(grid1)
        group2, d2 = self.visitall(grid2)
        ans = 0
        for groupname in d2:
            g2 = d2[groupname]
            i, j = groupname
            if group1[i][j] in d1:
                g1 = d1[group1[i][j]]
                if g2.issubset(g1):
                    ans += 1
        return ans


a = Solution()
print(
    a.countSubIslands(
        [
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
        ],
        [
            [1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
        ],
    )
)
print(
    a.countSubIslands(
        [
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
        ],
        [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ],
    )
)
