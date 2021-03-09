from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s  = abs(sum(nums) - goal)
        return (s + limit - 1) // limit
