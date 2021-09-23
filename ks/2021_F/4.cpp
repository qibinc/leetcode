#include <cstdio>
#include <map>

const int N = 20;
int n, m, k;
int l[N], r[N], a[N], edges[N];
std::map <int, int> cache;

int frontiers(int broken) {
    int ret = 0;
    for (int i = 0; i < n; i++) {
        if (broken & (1 << i)) {
            ret |= edges[i];
        }
    }
    return ret;
}

int recursive_count(long long points, int broken) {
    if (cache.count(broken)) {
        return cache[broken];
    }
    if (points > k) {
        return 0;
    }
    if (points == k) {
        return 1;
    }
    int ret = 0;
    int fs = frontiers(broken);
    for (int i = 0; i < n; i++) {
        if ((fs & (1 << i)) && ((broken & (1 << i)) == 0)) {
            if (l[i] <= points && points <= r[i]) {
                ret += recursive_count(points + a[i], broken | (1 << i));
            }
        }
    }
    cache[broken] = ret;
    return ret;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d%d%d", &n, &m, &k);
        cache.clear();
        for (int i = 0; i < n; i++) {
            edges[i] = 0;
            scanf("%d%d%d", &l[i], &r[i], &a[i]);
        }
        for (int i = 0; i < m; i++) {
            int x, y;
            scanf("%d%d", &x, &y);
            edges[x] |= 1 << y;
            edges[y] |= 1 << x;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += recursive_count(a[i], 1 << i);
        }
        printf("Case #%d: %d\n", t + 1, ans);
    }
    return 0;
}