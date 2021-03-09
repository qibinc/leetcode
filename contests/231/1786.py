from typing import Tuple, List, Dict
from collections import defaultdict, deque

class Solution:

    MOD = 10 ** 9 + 7

    def spfa(self, s: int, n: int, adj: Dict[int, List[Tuple[int, int]]]):
        q = deque([s])
        in_queue = [False] * n
        in_queue[s] = True
        distance = [21 * 10 ** 8] * n
        distance[s] = 0
        while q:
            x = q.popleft()
            in_queue[x] = False
            for y, w in adj[x]:
                if distance[x] + w < distance[y]:
                    distance[y] = distance[x] + w
                    if not in_queue[y]:
                        in_queue[y] = True
                        q.append(y)
        return distance

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x, y, w in edges:
            adj[x - 1].append((y - 1, w))
            adj[y - 1].append((x - 1, w))
        distance = self.spfa(n - 1, n, adj)
        distance_tup = [(d, i) for i, d in enumerate(distance)]
        distance_tup.sort()
        ans = [0] * n
        ans[n - 1] = 1
        for d, x in distance_tup:
            for y, w in adj[x]:
                if distance[y] > distance[x]:
                    ans[y] = (ans[y] + ans[x]) % Solution.MOD
        return ans[0]

a = Solution()
print(a.countRestrictedPaths(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))
print(a.countRestrictedPaths(7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))
        