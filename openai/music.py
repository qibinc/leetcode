# part1是：
# A 1 0 1 1 -> A2 A4 A4
# B 1 1 1 0 -> B4 B4 B2
# C 0 0 1 0 1 1 1 0 -> C4 C8 C8 C4

# part2是：
# A 1 0 1 1
# B 0 0 1 0
# -> A 2 <A B>4 A4

# A 1010
# B 1011
# C 0010
# <AB>2 <ABC>4 B4

from typing import List

def staff(beats_str: str) -> str:
    name, *beats = beats_str.split()
    beats = list(map(int, beats))

    i = 0
    while i < len(beats) and beats[i] == 0:
        i += 1
    j = i

    results = []
    while i < len(beats):
        j = i + 1
        while j < len(beats) and beats[j] == 0:
            j += 1
        
        length = j - i
        x = len(beats) // (1 << (length.bit_length() - 1))
        results.append(
            name + str(x)
        )

        i = j
        
    print(results)
    return " ".join(results)


def multi_staff(beats_str_list: List[str]) -> str:
    # parse
    beats_map = {}
    for beats_str in beats_str_list:
        name, *beats = beats_str.split()
        beats = list(map(int, beats))
        beats_map[name] = beats

    # pad
    max_length = max(len(l) for l in beats_map.values())
    for name in beats_map:
        if len(beats_map[name]) < max_length:
            assert max_length % (len(beats_map[name])) == 0
            mul = max_length // len(beats_map[name])
            beats_map[name] = sum([
                [v] + [0] * (mul - 1) for v in beats_map[name]
            ], start=[])

    i = 0
    # init
    while i < max_length and all(beats[i] == 0 for beats in beats_map.values()):
        i += 1
    j = i

    results = []
    while i < max_length:
        j = i + 1
        # find instructments of current beat
        names = [name for name in beats_map if beats_map[name][i] == 1]
        while j < max_length and all(beats_map[name][j] == 0 for name in names):
            j += 1
        
        length = j - i
        x = max_length // (1 << (length.bit_length() - 1))

        name = ("<" + "".join(names) + ">") if len(names) > 1 else names[0]
        results.append(name + str(x))

        # advance to next beat
        i += 1
        while i < max_length and all(beats[i] == 0 for beats in beats_map.values()):
            i += 1
        
    print(results)
    return " ".join(results)

if __name__ == "__main__":
    assert staff("A 1 0 1 1") == "A2 A4 A4"
    assert staff("A 1 0 0 1") == "A2 A4"
    assert staff("B 1 1 1 0") == "B4 B4 B2"
    assert staff("C 0 0 1 0 1 1 1 0") == "C4 C8 C8 C4"
    assert multi_staff([
        "A 1 0 1 1",
        "B 0 0 1 0",
    ]) == "A2 <AB>4 A4"
    assert multi_staff([
        "A 1 0 1 0",
        "B 1 0 1 1",
        "C 0 0 1 0",
    ]) == "<AB>2 <ABC>4 B4"
    assert multi_staff([
        "A 1 0 1 0",
        "B 1 0 1 1",
        "C 0 0 1 0 1 0 1 1",
    ]) == "<AB>2 C4 <ABC>4 <BC>8 C8"
    assert multi_staff([
        "A 0 0 1 0",
        "B 0 0 1 1",
        "C 0 0 1 0 1 0 1 1",
    ]) == "C4 <ABC>4 <BC>8 C8"

