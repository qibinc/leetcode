from dataclasses import dataclass
from typing import List, Tuple
from collections import defaultdict


@dataclass
class Sample:
    t: float
    stack: List[str]  # outermost -> innermost


def samples_to_trace(samples: List["Sample"], N: int) -> List[Tuple[float, str, str]]:
    if not samples:
        return []

    results: List[Tuple[float, str, str]] = []
    counts = defaultdict(int)  # (position, name) -> consecutive count

    def bump(pos: int, name: str, t: float) -> None:
        """Increment the consecutive count for (pos, name) and emit a start if it reaches N."""
        key = (pos, name)
        counts[key] += 1
        if counts[key] == N:
            results.append((t, "s", name))

    def end_and_clear(from_pos: int, t: float) -> None:
        """End and clear all active frames at positions >= from_pos."""
        for (p, name), cnt in list(counts.items()):
            if p >= from_pos:
                if cnt >= N:
                    results.append((t, "e", name))
                counts.pop((p, name))

    # Seed with the first sample
    s0 = samples[0]
    for pos, name in enumerate(s0.stack):
        bump(pos, name, s0.t)

    # Process subsequent samples
    for prev, cur in zip(samples, samples[1:]):
        t = cur.t

        # 1) Extend the matching prefix, bumping counts
        pos = 0
        for a, b in zip(prev.stack, cur.stack):
            if a != b:
                break
            bump(pos, b, t)
            pos += 1

        # 2) Close anything that diverged (or is beyond the prefix)
        end_and_clear(pos, t)

        # 3) Start counting any new frames from the divergence point
        for new_pos in range(pos, len(cur.stack)):
            name = cur.stack[new_pos]
            bump(new_pos, name, t)

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

    for trace in samples_to_trace(s2, N=3):
        print(trace)
