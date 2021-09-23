from functools import lru_cache, reduce

if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        n, m, k = tuple(map(int, input().strip().split()))
        rooms = []
        edges = [0] * n
        for _ in range(n):
            l, r, a = tuple(map(int, input().strip().split()))
            rooms.append((l, r, a))
        for _ in range(m):
            x, y = tuple(map(int, input().strip().split()))
            edges[x] |= 1 << y
            edges[y] |= 1 << x
        
        @lru_cache()
        def frontiers(broken):
            return reduce(lambda sa, sb: sa | sb, [edges[frontier] for frontier in range(n) if broken & (1 << frontier)])

        @lru_cache()
        def recursive_count(points: int, broken: int):
            if points == k:
                return 1
            ret = 0
            fs = frontiers(broken)
            for nxt in range(n):
                if (fs & (1 << nxt)) and (broken & (1 << nxt)) == 0:
                    if rooms[nxt][0] <= points and points <= rooms[nxt][1]:
                        nxt_tup = broken | (1 << nxt)
                        ret += recursive_count(points + rooms[nxt][2], nxt_tup)
            return ret
        
        ans = sum(recursive_count(rooms[i][2], 1 << i) for i in range(n))
        print(f"Case #{case + 1}: {ans}")
