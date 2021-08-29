from typing import List


class Solution:
    def dfs(self, num_sessions, time_left, task_left, alltime_left):
        if (
            num_sessions + ((alltime_left - time_left - 1) // self.sessionTime + 1)
            >= self.min_sessions
        ):
            return
        if task_left == 0:
            self.min_sessions = min(self.min_sessions, num_sessions)
            return
        for i, t in enumerate(self.tasks):
            if not self.assigned[i]:
                if time_left >= t:
                    self.assigned[i] = True
                    self.dfs(
                        num_sessions, time_left - t, task_left - 1, alltime_left - t
                    )
                    self.assigned[i] = False
                else:
                    self.assigned[i] = True
                    self.dfs(
                        num_sessions + 1,
                        self.sessionTime - t,
                        task_left - 1,
                        alltime_left - t,
                    )
                    self.assigned[i] = False

    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks = sorted(tasks, reverse=True)
        self.tasks = tasks
        self.assigned = [False] * len(tasks)
        self.min_sessions = len(tasks)
        self.sessionTime = sessionTime
        self.dfs(1, sessionTime, len(tasks), sum(tasks))
        return self.min_sessions


if __name__ == "__main__":
    a = Solution()
    print(a.minSessions([1, 2, 3], 3))
    print(a.minSessions([3, 1, 3, 1, 1], 8))
    print(a.minSessions([1, 2, 3, 4, 5], 15))
    print(a.minSessions(list(range(1, 15)), 15))
