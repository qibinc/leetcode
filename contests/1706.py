from typing import List

class Solution:
    def rollout(self, grid, idx):
        for line in grid:
            if line[idx] == 1:
                if line[idx + 1] == -1:
                    return -1
                else:
                    idx += 1
            else:
                if line[idx - 1] == 1:
                    return -1
                else:
                    idx -= 1
        return idx - 1

    def findBall(self, grid: List[List[int]]) -> List[int]:
        for line in grid:
            line.append(-1)
            line.insert(0, 1)
        ans = []
        for i in range(1, len(grid[0]) - 1):
            ans.append(self.rollout(grid, i))
        return ans
        
a = Solution()
print(a.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(a.findBall([[-1]]))