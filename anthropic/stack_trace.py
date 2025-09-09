from dataclasses import dataclass
from typing import List, Tuple
from collections import defaultdict


@dataclass
class Sample:
    t: float
    stack: List[str]  # outermost -> innermost


def samples_to_trace(samples: List[Sample], N: int) -> List[Tuple[float, str, str]]:
    if not samples: return []

    results = []
    counts = defaultdict(int)
    for pos, name in enumerate(samples[0].stack):
        counts[(pos, name)] += 1
        if counts[pos, name] == N:
            results.append((samples[0].t, "s", name))

    for idx in range(1, len(samples)):
        prev_sample = samples[idx - 1]
        sample = samples[idx]
        t = sample.t

        # match prefix traces
        pos = 0
        for a, b in zip(prev_sample.stack, sample.stack):
            if a == b:
                counts[pos, b] += 1
                if counts[pos, b] == N:
                    results.append((t, "s", b))
                pos += 1
            else:
                break

        for c_pos, c in list(counts.keys()):
            if c_pos >= pos:
                if counts[c_pos, c] >= N:
                    results.append((t, "e", c))
                counts.pop((c_pos, c))

        # add new traces
        for new_pos in range(pos, len(sample.stack)):
            counts[new_pos, sample.stack[new_pos]] = 1
            if counts[new_pos, sample.stack[new_pos]] == N:
                results.append((sample.t, "s", sample.stack[new_pos]))

    return results

if __name__ == "__main__":
    s2 = [
        Sample(0.0, ['a','b','a','c']),  # a -> b -> a -> c
        Sample(1.0, ['a','a','b','c']),
        Sample(2.0, ['a','a','b','c']),
        Sample(3.0, ['a','a','b','c']),
        Sample(4.0, ['a',]),
        Sample(5.0, ['a','a','b','c', "e"]),
    ]
    # (2.0, 's', 'a')
    # (3.0, 's', 'a')
    # (3.0, 's', 'b')
    # (3.0, 's', 'c')
    # (4.0, 'e', 'a')
    # (4.0, 'e', 'b')
    # (4.0, 'e', 'c')

    for trace in samples_to_trace(s2, N=1):
        print(trace)
