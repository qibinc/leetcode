int MOD = 1000000000 + 7;

int countPaths(int n, int **roads, int roadsSize, int *roadsColSize)
{
    long long **f = malloc(n * sizeof(long long *));
    long long **dist = malloc(n * sizeof(long long *));
    for (int i = 0; i < n; i++)
    {
        f[i] = malloc(n * sizeof(long long));
        dist[i] = malloc(n * sizeof(long long));
        f[i][i] = 1;
        dist[i][i] = 0;
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (i != j)
            {
                f[i][j] = 0;
                dist[i][j] = 1000000000000000000ll;
            }
    for (int i = 0; i < roadsSize; i++)
    {
        dist[roads[i][0]][roads[i][1]] = roads[i][2];
        dist[roads[i][1]][roads[i][0]] = roads[i][2];
        f[roads[i][0]][roads[i][1]] = 1;
        f[roads[i][1]][roads[i][0]] = 1;
    }
    for (int t = 0; t < n; t++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                if (i == j || t == i || t == j)
                    continue;
                if (dist[i][t] + dist[t][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][t] + dist[t][j];
                    f[i][j] = f[i][t] * f[t][j] % MOD;
                }
                else if (dist[i][t] + dist[t][j] == dist[i][j])
                    f[i][j] = (f[i][j] + f[i][t] * f[t][j]) % MOD;
            }
    return f[0][n - 1] % MOD;
}
