#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                o1 = stack.pop()
                o2 = stack.pop()
                if t == "/":
                    v = int(abs(o2) // abs(o1))
                    if o1 * o2 < 0:
                        v = -v
                else:
                    v = int(eval(str(o2) + t + str(o1)))
                stack.append(v)
            else:
                stack.append(int(t))
        return stack.pop()


# @lc code=end
