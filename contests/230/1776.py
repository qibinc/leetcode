from heapq import heappop, heappush
from typing import List

from dataclasses import dataclass

@dataclass
class Edge:
    prev: int
    next: int
    v1: int
    v2: int
    dis: float
    frontier: int
    last_t: int
    valid: bool
    
    @property
    def t(self):
        return self.dis / (self.v1 - self.v2 + 1e-30)

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        if len(cars) == 1:
            return [-1.]
        edges = []
        heap = []
        for i in range(len(cars) - 1):
            edge = Edge(i - 1, i + 1, cars[i][1], cars[i + 1][1], cars[i + 1][0] - cars[i][0], i, 0, True)
            edges.append(edge)
            if edge.t > 0:
                heappush(heap, (edge.t, i))
        edges[-1].next = 100000000
        
        ans = [-1.] * len(cars)
        while heap:
            t, idx = heappop(heap)
            if t > 1e10:
                break
            edge = edges[idx]
            if not (t > 0 and edge.valid):
                continue
            ans[edge.frontier] = t
            # merge edge
            edge.valid = False
            if edge.prev >= 0:
                # edge_prev need to be recalculated
                edge_prev = edges[edge.prev]
                edge_prev.valid = False
                new_dis = edge_prev.dis - (t - edge_prev.last_t) * (edge_prev.v1 - edge_prev.v2)
                new_edge = Edge(edge_prev.prev, edge.next, edge_prev.v1, edge.v2, new_dis, edge_prev.frontier, t, True)
                if new_edge.t >= -1e-8:
                    heappush(heap, (t + new_edge.t, len(edges)))
                if edge.next < len(edges):
                    edges[edge.next].prev = len(edges)
                if edge_prev.prev >= 0:
                    edges[edge_prev.prev].next = len(edges)
                edges.append(new_edge)
        return ans

