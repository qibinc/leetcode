from typing import List
from collections import defaultdict


class Solution:
    def serialize_dict(self, d):
        return f"{{{', '.join([f'({k}, {d[k]})' for k in d])}}}"

    def recursive_serialize(self, path, key, d):
        if d == {}:
            return f"{{}}"
        for key in d:
            d[key] = self.recursive_serialize(path + ", " + key, key, d[key])
        serialized = self.serialize_dict(d)
        self.count[serialized] += 1
        self.path_to_serailzed[path] = serialized
        return serialized

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        self.count = defaultdict(int)
        self.path_to_serailzed = {}
        tree_dict = {}
        for path in paths:
            d = tree_dict
            for folder in path:
                if folder not in d:
                    d[folder] = {}
                d = d[folder]
        self.recursive_serialize("l", "l", tree_dict)
        ans = []
        for path in paths:
            s = "l"
            removed = False
            for folder in path:
                s += ", " + folder
                if (
                    s in self.path_to_serailzed
                    and self.count[self.path_to_serailzed[s]] > 1
                ):
                    removed = True
                    break
            if not removed:
                ans.append(path)
        return ans


a = Solution()
print(
    a.deleteDuplicateFolder([["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]])
)
print(
    a.deleteDuplicateFolder(
        [
            ["a"],
            ["c"],
            ["a", "b"],
            ["c", "b"],
            ["a", "b", "x"],
            ["a", "b", "x", "y"],
            ["w"],
            ["w", "y"],
        ]
    )
)
print(a.deleteDuplicateFolder([["a", "b"], ["c", "d"], ["c"], ["a"]]))
print(
    a.deleteDuplicateFolder(
        [
            ["a"],
            ["a", "x"],
            ["a", "x", "y"],
            ["a", "z"],
            ["b"],
            ["b", "x"],
            ["b", "x", "y"],
            ["b", "z"],
        ]
    )
)
print(
    a.deleteDuplicateFolder(
        [
            ["a"],
            ["a", "x"],
            ["a", "x", "y"],
            ["a", "z"],
            ["b"],
            ["b", "x"],
            ["b", "x", "y"],
            ["b", "z"],
            ["b", "w"],
        ]
    )
)
