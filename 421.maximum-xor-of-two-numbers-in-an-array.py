class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for i in range(30, -1, -1):
            b = 1 << i
            mask |= b
            nans = ans | b
            s = set(nums[i] & mask for i in range(len(nums)))
            for x in s:
                if x ^ nans in s:
                    ans = nans
                    break
        return ans
