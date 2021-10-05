# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


vowels = set(["a", "e", "i", "o", "u"])


def calc_consonant_vowel(s, i, j):
    if i == j:
        return 0, 0
    elif i + 1 == j:
        return 1, int(s[i] in vowels)
    left, left_vow = calc_consonant_vowel(s, i, (i + j) // 2)
    right, right_vow = calc_consonant_vowel(s, (i + j) // 2, j)
    ret = abs(left_vow + right_vow - (j - i - left_vow - right_vow)) + left + right, left_vow + right_vow
    return ret


def solution(S):
    # write your code in Python 3.6
    return calc_consonant_vowel(S, 0, len(S))[0]

