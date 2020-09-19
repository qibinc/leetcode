class Solution:

    def __init__(self):
        self.candidates = []
        for length in range(2, 10):
            s = "".join(map(str, range(1, 10)))
            for i in range(10 - length):
                self.candidates.append(int(s[i: i + length]))

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return [
            cand
            for cand in self.candidates
            if low <= cand and cand <= high
        ]

