from typing import List
from functools import lru_cache


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        for idx in range(len(grid)):
            grid[idx] = list(grid[idx])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "C":
                    cat = i, j
                elif grid[i][j] == "M":
                    mouse = i, j
                elif grid[i][j] == "F":
                    self.food = i, j
        self.grid = grid
        self.n, self.m = len(grid), len(grid[0])
        self.catJump = catJump
        self.mouseJump = mouseJump
        ret = self.canMouseWinRecursive(cat, mouse, 0)
        return ret

    def inrange(self, x, y):
        return x >= 0 and y >= 0 and x < self.n and y < self.m

    @lru_cache(None)
    def canMouseWinRecursive(self, cat, mouse, step) -> bool:
        if step == 35:
            return False
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            for jump in range(1, self.mouseJump + 1):
                mx, my = mouse[0] + dx * jump, mouse[1] + dy * jump
                if (mx, my) == self.food:
                    return True
                if (mx, my) == cat:
                    continue
                if self.inrange(mx, my) and self.grid[mx][my] != "#":
                    if not self.canCatWinRecursive(
                        cat=cat, mouse=(mx, my), step=step + 1
                    ):
                        return True
                else:
                    break
        if not self.canCatWinRecursive(cat=cat, mouse=mouse, step=step + 1):
            return True
        return False

    @lru_cache(None)
    def canCatWinRecursive(self, cat, mouse, step) -> bool:
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            for jump in range(1, self.catJump + 1):
                cx, cy = cat[0] + dx * jump, cat[1] + dy * jump
                if (cx, cy) == self.food:
                    return True
                if (cx, cy) == mouse:
                    return True
                if self.inrange(cx, cy) and self.grid[cx][cy] != "#":
                    if not self.canMouseWinRecursive(
                        cat=(cx, cy), mouse=mouse, step=step
                    ):
                        return True
                else:
                    break
        if not self.canMouseWinRecursive(cat=cat, mouse=mouse, step=step):
            return True
        return False


a = Solution()
print(a.canMouseWin(["####F", "#C...", "M...."], 1, 2))
a = Solution()
print(a.canMouseWin(["M.C...F"], 1, 4))
a = Solution()
print(a.canMouseWin(["M.C...F"], 1, 3))
a = Solution()
print(a.canMouseWin(["C...#", "...#F", "....#", "M...."], 2, 5))
a = Solution()
print(a.canMouseWin([".M...", "..#..", "#..#.", "C#.#.", "...#F"], 3, 1))
a = Solution()
print(a.canMouseWin(["#..C...", "M....#.", "######F"], 1, 5))
a = Solution()
print(
    a.canMouseWin(
        [
            "CM......",
            "#######.",
            "........",
            ".#######",
            "........",
            "#######.",
            "........",
            "F#######",
        ],
        1,
        1,
    )
)
a = Solution()
print(a.canMouseWin(["#...", "....", ".C..", ".M.#", "....", "F..."], 3, 3))
a = Solution()
print(a.canMouseWin(["####.##", ".#C#F#.", "######.", "##M.###"], 3, 6))
