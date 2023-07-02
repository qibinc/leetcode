#
# @lc app=leetcode id=2662 lang=python3
#
# [2662] Minimum Cost of a Path With Special Roads
#

from typing import List

# @lc code=start
class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        nodes = (
            [tuple(start), tuple(target)]
            + [(tup[0], tup[1]) for tup in specialRoads]
            + [(tup[2], tup[3]) for tup in specialRoads]
        )
        nodes = list(set(nodes))
        node2id = {node: idx for idx, node in enumerate(nodes)}
        N = len(nodes)
        MAX = 10 ** 5 * 2
        distance = [[MAX] * N for _ in range(N)]
        for road in specialRoads:
            sid = node2id[(road[0], road[1])]
            tid = node2id[(road[2], road[3])]
            distance[sid][tid] = min(road[4], distance[sid][tid])
        for i in range(N):
            for j in range(N):
                xi, yi = nodes[i]
                xj, yj = nodes[j]
                distance[i][j] = min(distance[i][j], abs(xi - xj) + abs(yi - yj))

        d = [MAX] * N
        visited = [False] * N
        start_id = node2id[tuple(start)]
        d[start_id] = 0
        for i in range(N):
            k, dis = -1, MAX
            for j in range(N):
                if not visited[j] and d[j] < dis:
                    k, dis = j, d[j]

            for j in range(N):
                d[j] = min(d[j], d[k] + distance[k][j])
            visited[k] = True

        target_id = node2id[tuple(target)]
        # for row in distance:
        #     print(row)
        print(node2id)
        print(d)
        return d[target_id]


# @lc code=end

a = Solution()
# print(a.minimumCost([1, 1], [4, 5], [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]))
# print(
#     a.minimumCost([3, 2], [5, 7], [[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]])
# )
# print(
#     a.minimumCost(
#         [1, 1],
#         [4, 10],
#         [[1, 6, 2, 1, 2], [4, 2, 3, 8, 4], [2, 5, 1, 3, 5], [2, 4, 3, 8, 5]],
#     )
# )
# print(
#     a.minimumCost(
#         [1, 1],
#         [10, 4],
#         [[4, 2, 1, 1, 3], [1, 2, 7, 4, 4], [10, 3, 6, 1, 2], [6, 1, 1, 2, 3]],
#     )
# )
print(
    a.minimumCost(
        [1, 1],
        [1, 3],
        [
            [1, 1, 1, 3, 1],
            [1, 2, 1, 1, 2],
            [1, 1, 1, 3, 4],
            [1, 3, 1, 2, 5],
            [1, 2, 1, 3, 4],
        ],
    )
)
