class Solution:
    def minTimeToType(self, word: str) -> int:
        word = "a" + word
        return (
            sum(
                [
                    min(
                        (ord(word[i + 1]) - ord(word[i]) + 26) % 26,
                        (ord(word[i]) - ord(word[i + 1]) + 26) % 26,
                    )
                    for i in range(len(word) - 1)
                ]
            )
            + len(word)
            - 1
        )


a = Solution()
print(a.minTimeToType("abc"))
print(a.minTimeToType("bza"))
print(a.minTimeToType("zjpc"))
