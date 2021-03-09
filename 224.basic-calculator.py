#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def getunit(self, s):
        while self.idx < len(s) and s[self.idx] == " ":
            self.idx += 1
        if self.idx >= len(s):
            return ""
        ch = s[self.idx]
        self.idx += 1
        if ch in ["+", "-", "(", ")"]:
            return ch
        else:
            # digits
            ret = ch
            while self.idx < len(s) and s[self.idx] in set(map(str, range(10))):
                ret += s[self.idx]
                self.idx += 1
            return int(ret)

    def calculate(self, s: str) -> int:
        self.idx = 0
        operators = []
        def calc(op1, op2, op):
            if op == "+":
                return op1 + op2
            elif op == "-":
                return op1 - op2

        while (ch := self.getunit(s)) != "":
            if isinstance(ch, int):
                if not operators or operators[-1] == "(":
                    operators.append(ch)
                else:
                    op = operators.pop()
                    if operators and isinstance(operators[-1], int):
                        opr = operators.pop()
                    else:
                        opr = 0
                    operators.append(calc(opr, ch, op))
            elif ch in ["+", "-"]:
                operators.append(ch)
            elif ch == "(":
                operators.append(ch)
            elif ch == ")":
                opr = operators.pop()
                operators.pop()
                operators.append(opr)
                if len(operators) > 1 and operators[-2] != "(":
                    opr2 = operators.pop()
                    op = operators.pop()
                    if operators:
                        opr1 = operators.pop()
                    else:
                        opr1 = 0
                    operators.append(calc(opr1, opr2, op))

        return operators[0]

# @lc code=end

a = Solution()
print(a.calculate("((-1) + 1)"))
print(a.calculate(" 2-1 + 2 "))
print(a.calculate("(1+(4+5+2)-3)+(6+08)"))
print(a.calculate("((3))"))
print(a.calculate("0"))
