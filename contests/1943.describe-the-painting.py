from typing import List


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        loc_deltas = []
        for start, end, paint in segments:
            loc_deltas.append((start, paint))
            loc_deltas.append((end, -paint))
        loc_deltas.sort()
        ans = []
        curr_paint = 0
        last_loc = 0
        for loc, delta in loc_deltas:
            if loc != last_loc:
                if curr_paint > 0:
                    ans.append((last_loc, loc, curr_paint))
                last_loc = loc
            curr_paint += delta
        return ans


a = Solution()
print(a.splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]))
print(a.splitPainting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]))
print(a.splitPainting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]))
