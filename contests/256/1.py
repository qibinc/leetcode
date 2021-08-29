from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return min([nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1)])


if __name__ == "__main__":
    a = Solution()
    print(a.minimumDifference([90], 1))
    print(a.minimumDifference([9, 4, 1, 7], 2))
    print(a.minimumDifference([9, 4, 1, 7], 4))
