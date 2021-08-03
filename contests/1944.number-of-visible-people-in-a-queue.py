from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = []
        for height in reversed(heights):
            cnt = 0
            while stack and stack[-1] < height:
                cnt += 1
                stack.pop()
            cnt += len(stack) > 0
            while stack and stack[-1] == height:
                stack.pop()
            stack.append(height)
            ans.append(cnt)
        return list(reversed(ans))


a = Solution()
print(a.canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(a.canSeePersonsCount([5, 1, 2, 3, 10]))
print(a.canSeePersonsCount([5, 4, 3, 2, 1, 2, 3, 4, 5]))
