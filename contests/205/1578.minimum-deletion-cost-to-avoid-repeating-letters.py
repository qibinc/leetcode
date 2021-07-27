class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c = cost[0]
        sum = cost[0]
        cnt = 1
        ans = 0
        s += " "
        cost.append(0)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                c = max(c, cost[i])
                sum += cost[i]
            else:
                if cnt > 1:
                    ans += sum - c
                c = cost[i]
                sum = cost[i]
                cnt = 1
        return ans
