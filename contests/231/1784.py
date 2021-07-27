class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        met0 = False
        for ch in s:
            if ch == "0":
                met0 = True
            if ch == "1" and met0:
                return False
        return True
