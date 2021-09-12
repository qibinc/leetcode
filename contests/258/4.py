from typing import List, Dict
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


class Solution:
    def smallestMissingValueSubtree(
        self, parents: List[int], nums: List[int]
    ) -> List[int]:
        edges = defaultdict(list)
        for node, parent in enumerate(parents):
            edges[parent].append(node)
        results = {}
        num2node = {num: node for node, num in enumerate(nums)}
        union_parent = list(range(len(parents)))

        def find(node):
            if union_parent[node] != node:
                union_parent[node] = find(union_parent[node])
            return union_parent[node]

        def recursiveSmallestMissingValueSubtree(node: int) -> int:
            if node not in edges:
                results[node] = 2 if nums[node] == 1 else 1
                return results[node]
            missing_list = [
                recursiveSmallestMissingValueSubtree(child) for child in edges[node]
            ]
            for child in edges[node]:
                union_parent[find(child)] = union_parent[find(node)]
            max_missing = max(missing_list)
            while max_missing in num2node and find(num2node[max_missing]) == find(node):
                max_missing += 1
            results[node] = max_missing
            return max_missing

        recursiveSmallestMissingValueSubtree(0)
        return [results[i] for i in range(len(nums))]


a = Solution()
print(a.smallestMissingValueSubtree([-1, 0, 0, 2], [1, 2, 3, 4]))
print(a.smallestMissingValueSubtree([-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3]))
print(a.smallestMissingValueSubtree([-1, 2, 3, 0, 2, 4, 1], [2, 3, 4, 5, 6, 7, 8]))
