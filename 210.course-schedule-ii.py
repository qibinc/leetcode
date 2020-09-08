#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        adj = [[] for _ in range(numCourses)]
        d = [0] * numCourses
        for e in prerequisites:
            adj[e[1]].append(e[0])
            d[e[0]] += 1
        for i, k in enumerate(d):
            if k == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for e in adj[node]:
                d[e] -= 1
                if d[e] == 0:
                    q.append(e)
        if not any(d):
            return ans
        else:
            return []
        
# @lc code=end

