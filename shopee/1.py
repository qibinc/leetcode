import json


class Node(object):

    MAX = -(10 ** 30)

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def construct(cls, arr, idx):
        if idx >= len(arr) or arr[idx] == "null":
            return None
        return Node(
            int(arr[idx]),
            cls.construct(arr, idx * 2 + 1),
            cls.construct(arr, idx * 2 + 2),
        )

    def find_max(self):
        left_max = max(self.left.find_max() if self.left is not None else 0, 0)
        right_max = max(self.right.find_max() if self.right is not None else 0, 0)
        ret = self.val + max(left_max, 0) + max(right_max, 0)
        if ret > Node.MAX:
            Node.MAX = ret
        return self.val + max(left_max, right_max, 0)

    def __str__(self):
        return f"Node({self.val}, {self.left}, {self.right})"


if __name__ == "__main__":
    s = input().replace("null", '"null"')
    elements = json.loads(s)
    root = Node.construct(elements, 0)
    root.find_max()
    print(Node.MAX)
