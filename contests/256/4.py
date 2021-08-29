MOD = 10 ** 9 + 7


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        ans = 0
        if "0" in binary:
            ans += 1
        if "1" not in binary:
            return 1
        binary = binary[binary.index("1") :]
        end_0 = 0
        end_1 = 1
        for ch in binary[1:]:
            if ch == "1":
                end_1 = (end_1 + end_0 + 1) % MOD
            else:
                end_0 = (end_0 + end_1) % MOD
        return (ans + end_1 + end_0) % MOD


if __name__ == "__main__":
    a = Solution()
    print(a.numberOfUniqueGoodSubsequences("0"))
    print(a.numberOfUniqueGoodSubsequences("1"))
    print(a.numberOfUniqueGoodSubsequences("011"))
    print(a.numberOfUniqueGoodSubsequences("11"))
    print(a.numberOfUniqueGoodSubsequences("111"))
    print(a.numberOfUniqueGoodSubsequences("1111"))
    print(a.numberOfUniqueGoodSubsequences("11111"))
    print(a.numberOfUniqueGoodSubsequences("001"))
    print(a.numberOfUniqueGoodSubsequences("101"))
    print(a.numberOfUniqueGoodSubsequences("10"))
    print(a.numberOfUniqueGoodSubsequences("100"))
    print(a.numberOfUniqueGoodSubsequences("1000"))
    print(a.numberOfUniqueGoodSubsequences("10101"))
