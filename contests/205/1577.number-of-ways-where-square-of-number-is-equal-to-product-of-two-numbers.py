class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.numTriplets1(nums1, nums2) + self.numTriplets1(nums2, nums1)

    def numTriplets1(self, nums1: List[int], nums2: List[int]) -> int:
        d = defaultdict(int)
        for x in nums1:
            d[x * x] += 1
        ans = 0
        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                t = nums2[j] * nums2[k]
                if t in d:
                    ans += d[t]
        return ans
