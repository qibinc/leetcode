#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from collections import deque


class Solution:
    DIRETIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        for i in range(len(board)):
            if board[i][0] == "O":
                self.fill(board, i, 0)
            if board[i][len(board[0]) - 1] == "O":
                self.fill(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.fill(board, 0, j)
            if board[len(board) - 1][j] == "O":
                self.fill(board, len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "1":
                    board[i][j] = "O"

    def fill(self, board, x, y) -> None:
        q = deque([(x, y)])
        board[x][y] = "1"
        while q:
            x, y = q.popleft()
            for dx, dy in self.DIRETIONS:
                newx = x + dx
                newy = y + dy
                if (
                    newx >= 0
                    and newx < len(board)
                    and newy >= 0
                    and newy < len(board[0])
                    and board[newx][newy] == "O"
                ):
                    board[newx][newy] = "1"
                    q.append((newx, newy))


# @lc code=end
