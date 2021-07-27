class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        pref_list = []
        for pref in preferences:
            pref_list.append([0] * n)
            for i, fri in enumerate(pref):
                pref_list[-1][fri] = -i
        happy = [True] * n
        for idx, p1 in enumerate(pairs):
            for p2 in pairs[idx + 1 :]:
                x, y = p1
                u, v = p2
                self.check(pref_list, happy, x, y, u, v)
                y, x = p1
                u, v = p2
                self.check(pref_list, happy, x, y, u, v)
                x, y = p1
                v, u = p2
                self.check(pref_list, happy, x, y, u, v)
                y, x = p1
                v, u = p2
                self.check(pref_list, happy, x, y, u, v)
        return n - sum(happy)

    def check(self, pref_list, happy, x, y, u, v):
        if pref_list[x][y] < pref_list[x][u] and pref_list[u][v] < pref_list[u][x]:
            happy[x] = False
            happy[u] = False
