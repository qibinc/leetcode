#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        for i in range(len(gas)):
            gas[i] -= cost[i]
        i, j = 0, 1
        v = gas[0]
        while j % len(gas) != (i + len(gas)) % len(gas):
            while v >= 0 and j % len(gas) != (i + len(gas)) % len(gas):
                v += gas[j % len(gas)]
                j += 1
            while v < 0 and j % len(gas) != (i + len(gas)) % len(gas):
                v += gas[(i - 1 + len(gas)) % len(gas)]
                i -= 1
        if v >= 0:
            return j % len(gas)
        else:
            return -1


# @lc code=end
