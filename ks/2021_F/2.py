from heapq import heapify, heappush, heappop
from collections import defaultdict

def validate_heaptop(hp, valid):
    if not hp:
        return hp
    while hp and not valid[hp[0][1]]:
        _, _ = heappop(hp)
    return hp

if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        d, n, k = map(int, input().strip().split())
        start = defaultdict(list)
        end = defaultdict(list)
        for i in range(n):
            h, s, e = map(int, input().strip().split())
            start[s].append((h, i))
            end[e].append((h, i))
        max_k_min_heap = []
        k_sum = 0
        k_num = 0
        remaining_max_heap = []
        valid = [True] * n
        in_k = [False] * n
        ans = 0
        for i in range(1, d + 1):
            for h, idx in start[i]:
                validate_heaptop(max_k_min_heap, valid)
                if k_num < k:
                    k_num += 1
                    k_sum += h
                    in_k[idx] = True
                    heappush(max_k_min_heap, (h, idx))
                elif max_k_min_heap[0][0] < h:
                    replaced_h, replaced_idx = heappop(max_k_min_heap)
                    in_k[replaced_idx] = False
                    k_sum -= replaced_h

                    heappush(max_k_min_heap, (h, idx))
                    in_k[idx] = True
                    k_sum += h

                    heappush(remaining_max_heap, (-replaced_h, replaced_idx))
                else:
                    heappush(remaining_max_heap, (-h, idx))

            ans = max(ans, k_sum)
            for h, idx in end[i]:
                valid[idx] = False
                if in_k[idx]:
                    k_num -= 1
                    k_sum -= h
                    in_k[idx] = False
            while k_num < k and validate_heaptop(remaining_max_heap, valid):
                h, idx = heappop(remaining_max_heap)
                heappush(max_k_min_heap, (-h, idx))
                k_num += 1
                k_sum += -h
                in_k[idx] = True

        print(f"Case #{case + 1}: {ans}")
