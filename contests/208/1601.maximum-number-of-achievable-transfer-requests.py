class Solution:
    def check(self, n, reqs, choices):
        deg = [0] * n
        for req, choice in zip(reqs, choices):
            if choice:
                deg[req[0]] += 1
                deg[req[1]] -= 1
        return not any(deg)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_req = 0
        for i in range(1 << len(requests)):
            t = i
            choices = [int(bool(i & (1 << j))) for j in range(len(requests))]
            if self.check(n, requests, choices):
                if sum(choices) > max_req:
                    max_req = sum(choices)
        return max_req
