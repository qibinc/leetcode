class Solution:
    def largestOddNumber(self, num: str) -> str:
        for idx, ch in enumerate(reversed(num)):
            if int(ch) & 1:
                return num[: len(num) - idx]
        return ""
