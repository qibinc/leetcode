# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, Y, Z):
    i, j = 0, 0
    arr = []
    while j < len(S):
        while j < len(S) and S[j] != "\n":
            j += 1
        if j < len(S):
            j += 1
        arr.append(list(S[i:j]))
        i = j

    t = 0
    for i in range(len(arr)):
        if t <= Y and Y < t + len(arr[i]):
            t = Y - t
            break
        t += len(arr[i])
    prev = []
    if i > 0:
        prev += arr[i - 1]
    prev += arr[i][:t]
    prev = prev[max(0, len(prev)-Z):]
    nxt = []
    nxt += arr[i][t + 1:]
    if i < len(arr) - 1:
        nxt += arr[i + 1]
    nxt = nxt[:Z]

    if "\n" in prev:
        pos = prev.index("\n") + 1
    else:
        pos = 0
    idx_error = len(prev) - pos
    blank_line = " " * idx_error + "^\n"
    ans = "".join(prev) + arr[i][t]
    if arr[i][t] == "\n":
        ans += blank_line + "".join(nxt)
    elif "\n" in nxt:
        ans += "".join(nxt[:nxt.index("\n") + 1]) + blank_line + "".join(nxt[nxt.index("\n") + 1:])
    else:
        ans += "\n" + blank_line
    return ans


# print(solution('// comment\nint main() {\n    return 0\n}\n', 36, 126))
# s = '123\nasdf\n123\n456\n123\n\nasdf\n'
# print(solution(s, len(s) - 6, 3))
# print(solution('\n123\n1243', 8, 5))
# print(solution('// comment\nint main() {\n    return 0\n}\n', 23, 126))
# print(solution('// comment\nint main() {\n    return 0\n}\n', 24, 126))
# print(solution('// comment\nint main() {\n    return 0\n}\n', 0, 126))
# s = '// comment\nint main() {\n    return 0\n}\n'
# print(solution('// comment\nint main() {\n    return 0\n}\n', len(s) - 1, 126))

