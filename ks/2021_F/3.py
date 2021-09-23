import math
import functools

MAX = 10 ** 9


@functools.lru_cache()
def cross_prod(a, b):
    a_x, a_y = a
    b_x, b_y = b
    print(a, b)
    return a_x * b_y - a_y * b_x


@functools.lru_cache()
def diff(s, t):
    s_x, s_y = s
    t_x, t_y = t
    return t_x - s_x, t_y - s_y


@functools.lru_cache()
def dist(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)


if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        n = int(input())
        positions = []
        for i in range(n):
            positions.append(tuple(map(int, input().strip().split())))
        blue_x, blue_y = tuple(map(int, input().strip().split()))
        ans = MAX
        # triangles
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (
                        cross_prod(
                            diff(positions[i], positions[j]),
                            diff(positions[i], (blue_x, blue_y)),
                        )
                        * cross_prod(
                            diff(positions[i], positions[k]),
                            diff(positions[i], (blue_x, blue_y)),
                        )
                        < 0
                        and cross_prod(
                            diff(positions[j], positions[i]),
                            diff(positions[j], (blue_x, blue_y)),
                        )
                        * cross_prod(
                            diff(positions[j], positions[k]),
                            diff(positions[j], (blue_x, blue_y)),
                        )
                        < 0
                    ):
                        print(i, j, k)
                        ans = min(
                            ans,
                            dist(positions[i], positions[j])
                            + dist(positions[i], positions[k])
                            + dist(positions[j], positions[k]),
                        )
            # quadrilateral
        for i in range(n):
            for j in range(i + 1, n):
                if (
                    cross_prod(
                        diff(positions[i], positions[j]),
                        diff(positions[i], (blue_x, blue_y)),
                    )
                    != 0
                ):
                    continue
                min_1, min_2 = MAX, MAX
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if (
                        cross_prod(
                            diff(positions[k], positions[i]),
                            diff(positions[k], (blue_x, blue_y)),
                        )
                        * cross_prod(
                            diff(positions[k], positions[j]),
                            diff(positions[k], (blue_x, blue_y)),
                        )
                        < 0
                    ):
                        cpd = cross_prod(
                            diff(positions[i], positions[j]),
                            diff(positions[i], positions[k]),
                        ) 
                        if cpd < 0:
                            min_1 = min(min_1, dist(positions[k], positions[i]) + dist(positions[k], positions[j]))
                        elif cpd > 0:
                            min_2 = min(min_2, dist(positions[k], positions[i]) + dist(positions[k], positions[j]))
                ans = min(ans, min_1 + min_2)

        if ans == MAX:
            print(f"Case #{case + 1}: IMPOSSIBLE")
        else:
            print(f"Case #{case + 1}: {ans:.6f}")
