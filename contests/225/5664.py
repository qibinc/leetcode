from itertools import accumulate


class Solution:
    def bs(self, arr, l, r, v):
        while l < r - 1:
            mid = (l + r) >> 1
            if arr[mid] > v:
                r = mid
            else:
                l = mid
        return l

    def minimumBoxes(self, n: int) -> int:
        arr = []
        for i in range(1, 40000):
            arr.append((1 + i) * i // 2)
        sarr = list(accumulate(arr))
        idx = self.bs(sarr, 0, len(sarr), n)
        n -= sarr[idx]
        if n == 0:
            return (1 + (idx + 1)) * (idx + 1) // 2
        else:
            nidx = self.bs(arr, 0, idx + 1, n)
            if n > arr[nidx]:
                nidx += 1
            return (1 + (idx + 1)) * (idx + 1) // 2 + nidx + 1


a = Solution()
print(a.minimumBoxes(207818))
