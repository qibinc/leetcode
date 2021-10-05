# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

direction = {
    '<': (0, -1),
    '>': (0, 1), 
    '^': (-1, 0), 
    'v': (1, 0)
}

def solution(b):
    # write your code in Python 3.6
    n, m = len(b), len(b[0])
    for i in range(n):
        b[i] = list(b[i])
    starti, startj = None, None
    for i in range(n):
        for j in range(m):
            if b[i][j] in direction.keys():
                di, dj = direction[b[i][j]]
                xi, xj = i + di, j + dj
                while 0 <= xi and xi < n and 0 <= xj and xj < m and b[xi][xj] not in direction.keys() and b[xi][xj] != "X":
                    b[xi][xj] = "Y"
                    xi, xj = xi + di, xj + dj
            if b[i][j] == "A":
                starti, startj = i, j
    if starti is None or b[starti][startj] == "Y":
        return False

    visit = [[False] * m for _ in range(n)]
    visit[starti][startj] = True
    q = deque([(starti, startj)])
    while q:
        i, j = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xi, xj = i + di, j + dj
            if 0 <= xi and xi < n and 0 <= xj and xj < m and b[xi][xj] == "." and not visit[xi][xj]:
                visit[xi][xj] = True
                q.append((xi, xj))
    return visit[n - 1][m - 1]
