#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        f = [0, 1]
        p2, p3, p5 = 1, 1, 1
        for _ in range(2, n + 1):
            m = min(2 * f[p2], 3 * f[p3], 5 * f[p5])
            if m == 2 * f[p2]:
                p2 += 1
            if m == 3 * f[p3]:
                p3 += 1
            if m == 5 * f[p5]:
                p5 += 1
            f.append(m)

        return f[-1]


# @lc code=end

a = Solution()
print(a.nthUglyNumber(1))
print(a.nthUglyNumber(10))
print(a.nthUglyNumber(100))
# print(a.nthUglyNumber(1690))
