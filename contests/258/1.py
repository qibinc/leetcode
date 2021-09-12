class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        return word[: word.index(ch) + 1][::-1] + word[word.index(ch) + 1 :]


a = Solution()
print(a.reversePrefix("abcdefd", "d"))
print(a.reversePrefix("xyxzxe", "z"))
print(a.reversePrefix("abcd", "z"))
