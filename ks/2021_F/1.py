
if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        n = int(input())
        positions = input().strip()
        next = [10 ** 9] * (n + 1)
        for i in reversed(range(n)):
            if positions[i] == '1':
                next[i] = i
            else:
                next[i] = next[i + 1]
        ans = 0
        prev = - 10 ** 9
        for i in range(n):
            ans += min(i - prev, next[i] - i)
            if positions[i] == '1':
                prev = i
        print(f"Case #{case + 1}: {ans}")
            