#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not self.visited[i][j]:
                    cnt += 1
                    self.flood(grid, i, j)
        return cnt

    def flood(self, grid, x, y):
        self.visited[x][y] = True
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if (
                nx >= 0
                and ny >= 0
                and nx < len(grid)
                and ny < len(grid[0])
                and grid[nx][ny] == "1"
                and not self.visited[nx][ny]
            ):
                self.flood(grid, nx, ny)


# @lc code=end
