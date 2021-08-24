# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# ()(()


def longest_valid_substring(s: str) -> int:
    stack = []
    left_to_right = [-1] * len(s)
    for idx, ch in enumerate(s):
        if ch == "(":
            stack.append((ch, idx))
        elif stack:
            # non-empty
            _, left_idx = stack.pop()
            left_to_right[left_idx] = idx

    max_len = 0
    current_len = 0
    idx = 0
    while idx < len(s):
        right_idx = left_to_right[idx]
        if right_idx != -1:
            current_len += right_idx - idx + 1
            max_len = max(max_len, current_len)
            idx = right_idx + 1
        else:
            current_len = 0
            idx += 1
    return max_len


print(longest_valid_substring("()(()"))
print(longest_valid_substring("()(())"))
print(longest_valid_substring("()"))
print(longest_valid_substring("(()())"))
print(longest_valid_substring("("))
print(longest_valid_substring(")"))
print(longest_valid_substring(""))
print(longest_valid_substring("((((((((()()(())"))
print(longest_valid_substring("())))))"))
