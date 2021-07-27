class Solution:
    @staticmethod
    def f(time: str):
        return int(time[:2]) * 4 + (int(time[-2:]) + 14) // 15

    @staticmethod
    def g(time: str):
        return int(time[:2]) * 4 + int(time[-2:]) // 15

    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        if (
            int(startTime[:2]) > int(finishTime[:2])
            or int(startTime[:2]) == int(finishTime[:2])
            and int(startTime[-2:]) > int(finishTime[-2:])
        ):
            finishTime = str(int(finishTime[:2]) + 24) + finishTime[2:]
        start = self.f(startTime)
        end = self.g(finishTime)
        return end - start


a = Solution()
print(a.numberOfRounds("12:01", "12:44"))
print(a.numberOfRounds("20:00", "06:00"))
print(a.numberOfRounds("00:00", "23:59"))
print(a.numberOfRounds("23:59", "23:58"))
print(a.numberOfRounds("00:59", "01:01"))
