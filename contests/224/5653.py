class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = max(min(x) for x in rectangles)
        return sum([min(x) == max_len for x in rectangles])
