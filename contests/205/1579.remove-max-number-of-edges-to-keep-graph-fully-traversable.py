class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        pa = list(range(n + 1))
        edges.sort(key=lambda x: -x[0])
        ans = 0
        x = False
        for idx, (t, i, j) in enumerate(edges):
            self.compress(pa, i)
            self.compress(pa, j)
            if pa[i] == pa[j]:
                continue
            if t == 3:
                self.merge(pa, i, j)
                ans += 1
            else:
                x = True
                break

        pa = [pa, pa.copy()]
        if x:
            for t, i, j in edges[idx:]:
                t = t - 1
                self.compress(pa[t], i)
                self.compress(pa[t], j)
                if pa[t][i] == pa[t][j]:
                    continue
                self.merge(pa[t], i, j)
                ans += 1

        for k in [0, 1]:
            num = 0
            for i in range(1, n + 1):
                self.compress(pa[k], i)
                if pa[k][i] == i:
                    num += 1
            if num > 1:
                return -1

        return len(edges) - ans

    def compress(self, pa, i):
        ti = i
        while pa[ti] != ti:
            ti = pa[ti]
        while pa[i] != i:
            ni = pa[i]
            pa[i] = ti
            i = ni

    def merge(self, pa, i, j):
        self.compress(pa, i)
        self.compress(pa, j)
        i = pa[i]
        j = pa[j]
        pa[j] = i

