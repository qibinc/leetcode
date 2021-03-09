from typing import List
from itertools import accumulate

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = list(map(int, boxes))
        prefix = list(accumulate(boxes))
        prefix_ops = [0]
        for i in range(1, len(boxes)):
            prefix_ops.append(prefix_ops[-1] + prefix[i - 1])
        ans = []
        suf_ops = 0
        suf = 0
        for i in reversed(range(len(boxes))):
            ans.append(prefix_ops[i] + suf_ops)
            suf += boxes[i]
            suf_ops += suf
        return list(reversed(ans))

a = Solution()
print(a.minOperations("0"))
print(a.minOperations("001011"))
