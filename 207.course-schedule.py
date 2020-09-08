#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        adj = [[] for _ in range(numCourses)]
        d = [0] * numCourses
        for e in prerequisites:
            adj[e[1]].append(e[0])
            d[e[0]] += 1
        for i, k in enumerate(d):
            if k == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for e in adj[node]:
                d[e] -= 1
                if d[e] == 0:
                    q.append(e)
        return not any(d)

        
# @lc code=end

