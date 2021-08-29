class Solution:
    N_CHARS = 26
    MOD = 10 ** 9 + 7

    def left_to_right(self, right_hash, multipliers, i, j):
        "Compute the hash value of s[i, j]"
        ret = (
            (right_hash[i] - right_hash[j + 1] * multipliers[j - i + 1]) % Solution.MOD
            + Solution.MOD
        ) % Solution.MOD
        return ret

    def right_to_left(self, left_hash, multipliers, i, j):
        "Compute the hash value of reversed(s[i, j])"
        ret = (
            (left_hash[j + 1] - left_hash[i] * multipliers[j - i + 1]) % Solution.MOD
            + Solution.MOD
        ) % Solution.MOD
        return ret

    def maxProduct(self, s: str) -> int:
        left_hash = [0]
        for i in range(len(s)):
            left_hash.append(
                (left_hash[-1] * Solution.N_CHARS + ord(s[i]) - ord("a")) % Solution.MOD
            )
        right_hash = [0]
        for i in reversed(range(len(s))):
            right_hash.append(
                (right_hash[-1] * Solution.N_CHARS + ord(s[i]) - ord("a"))
                % Solution.MOD
            )
        right_hash = right_hash[::-1]
        multipliers = [1]
        for i in range(len(s)):
            multipliers.append(multipliers[-1] * Solution.N_CHARS % Solution.MOD)
        max_length = 1
        left_palindromic = [1, 1]
        for i in range(2, len(s)):
            if i - max_length - 2 + 1 >= 0 and self.left_to_right(
                right_hash, multipliers, i - max_length - 2 + 1, i
            ) == self.right_to_left(left_hash, multipliers, i - max_length - 2 + 1, i):
                max_length += 2
            left_palindromic.append(max_length)
        max_length = 1
        right_palindromic = [1, 1]
        for i in reversed(range(len(s) - 2)):
            if i + max_length + 2 - 1 < len(s) and self.left_to_right(
                right_hash, multipliers, i, i + max_length + 2 - 1
            ) == self.right_to_left(left_hash, multipliers, i, i + max_length + 2 - 1):
                max_length += 2
            right_palindromic.append(max_length)
        right_palindromic = right_palindromic[::-1]
        ans = 0
        for i in range(len(s) - 1):
            if left_palindromic[i] * right_palindromic[i + 1] > ans:
                ans = left_palindromic[i] * right_palindromic[i + 1]
        return ans
