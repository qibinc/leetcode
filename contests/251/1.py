class Solution:

    def transform(self, s):
        return str(sum(map(lambda x: int(x), list(s))))

    def getLucky(self, s: str, k: int) -> int:
        num_s = ""
        for ch in s:
            num_s += str(ord(ch) - ord('a') + 1)
        for i in range(k):
            num_s = self.transform(num_s)
        return int(num_s)


a = Solution()
print(a.getLucky("iiii", 1))