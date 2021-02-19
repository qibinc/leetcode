#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
from typing import List
from collections import defaultdict
from heapq import heapify, heappop, heappush

class Magic:
    def __init__(self, buildings) -> None:
        self.buildings = buildings
        self.valid = [False] * len(buildings)
        self.q = []

    def add(self, idx):
        heappush(self.q, (-self.buildings[idx][2], idx))
        self.valid[idx] = True

    def remove(self, idx):
        self.valid[idx] = False

    def top(self):
        while self.q:
            height, idx = self.q[0]
            if self.valid[idx]:
                return -height
            heappop(self.q)
        if not self.q:
            return 0

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = [[-1, 0]]
        start_at = defaultdict(list)
        end_at = defaultdict(list)
        for idx, (start, end, height) in enumerate(buildings):
            start_at[start].append(idx)
            end_at[end].append(idx)
        positions = sorted(list(set(list(start_at.keys()) + list(end_at.keys()))))
        q = Magic(buildings)
        for pos in positions:
            _, prev_height = ans[-1]
            for idx in end_at[pos]:
                q.remove(idx)
            for idx in start_at[pos]:
                q.add(idx)
            height = q.top()
            if height != prev_height:
                ans.append((pos, height))
        return ans[1:]
        
# @lc code=end


a = Solution()
print(a.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(a.getSkyline([[0,2,3],[2,5,3]]))
