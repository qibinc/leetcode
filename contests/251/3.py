from typing import List

class Solution:
    def compute(self, arr1, arr2) -> int:
        return sum([x == y for x, y in zip(arr1, arr2)])

    def score(self, assigned, compatibility) -> int:
        return sum([compatibility[i][x] for i, x in enumerate(assigned)])

    def dfs(self, idx, assigned, compatibility):
        if idx == len(assigned):
            return self.score(assigned, compatibility)
        
        best = 0
        for i in range(len(assigned)):
            if assigned[i] == -1:
                assigned[i] = idx
                ret = self.dfs(idx + 1, assigned, compatibility)
                assigned[i] = -1
                if ret > best:
                    best = ret
        return best

    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        compatibility = [[0] * len(mentors) for _ in range(len(students))]
        for i in range(len(students)):
            for j in range(len(mentors)):
                compatibility[i][j] = self.compute(students[i], mentors[j])
        assigned = [-1] * len(students)
        return self.dfs(0, assigned, compatibility)

a = Solution()
# print(a.maxCompatibilitySum([[1,1,0],[1,0,1],[0,0,1]], [[1,0,0],[0,0,1],[1,1,0]]))
print(a.maxCompatibilitySum([[1,1],[1,1],[1,1]], [[0,0],[0,0],[0,0]]))
