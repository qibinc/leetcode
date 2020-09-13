class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = [float(inf)] * len(points)
        d[0] = 0
        v = [False] * len(points)
        for i in range(1, len(points)):
            dis = float(inf)
            for j in range(len(points)):
                if d[j] < dis and not v[j]:
                    dis = d[j]
                    k = j
            # expand from k
            v[k] = True
            for j in range(len(points)):
                if not v[j] and abs(points[j][0] - points[k][0]) + abs(points[j][1] - points[k][1]) < d[j]:
                    d[j] = abs(points[j][0] - points[k][0]) + abs(points[j][1] - points[k][1])
        return sum(d)

