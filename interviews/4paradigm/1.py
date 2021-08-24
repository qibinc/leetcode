# 平衡数的定义是：将一个数分成左右两部分，分别成为两个新的数。
# 左右部分必须满足以下两点：
# 1，左边和右边至少存在一位。
# 2，左边的数每一位相乘如果等于右边的数每一位相乘，则这个数称为平衡数。
# 例如：1221这个数，分成12和21的话，1*2=2*1，则称1221为平衡数，再例如：1236这个数，可以分成123和1*2*3=6，所以1236也是平衡数。而1234无论怎样分也不满足平衡数。
# 输入描述
# 输入一个正整数（int范围内）。
# 输出描述
# 如果该数是平衡数，输出 "YES", 否则输出 "NO"。


def balanced_number(num: int) -> bool:
    num_str = str(num)
    num_zeros = len(list(filter(lambda x: x == "0", list(num_str))))
    if len(num_str) <= 1:
        return False
    if num_zeros == 1:
        return False
    elif num_zeros > 1:
        return True
    suffix_multi = 1
    for ch in num_str:
        suffix_multi *= int(ch)
    prefix_multi = 1
    for ch in num_str:
        prefix_multi *= int(ch)
        suffix_multi //= int(ch)
        if prefix_multi == suffix_multi:
            return True
    return False


print(balanced_number(1221))
print(balanced_number(1236))
print(balanced_number(12341236))
print(balanced_number(0))
print(balanced_number(10))
print(balanced_number(100))
print(balanced_number(1))
print(balanced_number(2))
