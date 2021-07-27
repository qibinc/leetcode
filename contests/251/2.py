from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans = ""
        used = False
        for x in num:
            if change[int(x)] == int(x):
                ans += x
            elif change[int(x)] > int(x):
                ans += str(change[int(x)])
                used = True
            else:
                if used:
                    break
                ans += x
        if len(ans) < len(num):
            ans += num[len(ans) - len(num) :]
        return ans


a = Solution()
print(a.maximumNumber("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]))
