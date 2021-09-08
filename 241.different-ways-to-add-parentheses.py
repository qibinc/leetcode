#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

from typing import List, Callable

# @lc code=start
class Solution:
    def recursive_compute(self, numbers, operators) -> List[int]:
        if len(numbers) == 1:
            return numbers
        results = []
        for idx, op in enumerate(operators):
            left = self.recursive_compute(numbers[: idx + 1], operators[:idx])
            right = self.recursive_compute(numbers[idx + 1 :], operators[idx + 1 :])
            op = operators[idx]
            results += [op(x, y) for x in left for y in right]
        return results

    def diffWaysToCompute(self, expression: str) -> List[int]:
        numbers: List[int] = list(
            map(
                int,
                (
                    expression.replace("+", " ")
                    .replace("-", " ")
                    .replace("*", " ")
                    .split()
                ),
            )
        )
        operators: List[Callable[[int, int], int]] = list(
            map(
                lambda op_str: {
                    "+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y,
                }[op_str],
                filter(lambda x: x in ["+", "-", "*"], expression),
            )
        )
        assert len(numbers) == len(operators) + 1
        return self.recursive_compute(numbers, operators)


# @lc code=end

a = Solution()
print(a.diffWaysToCompute("2-1-1"))
print(a.diffWaysToCompute("2*3-4*5"))
# print(a.diffWaysToCompute("1+1+1+1+1+1+1+1+1+1"))
