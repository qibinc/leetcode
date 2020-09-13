class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        s_row = []
        for i in range(len(mat)):
            s_row.append(0)
            for j in range(len(mat[0])):
                s_row[-1] += mat[i][j]
        s_col = []
        for j in range(len(mat[0])):
            s_col.append(0)
            for i in range(len(mat)):
                s_col[-1] += mat[i][j]
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if s_row[i] == 1 and s_col[j] == 1 and mat[i][j] == 1:
                    ans += 1
        return ans
