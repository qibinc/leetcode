from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Sample:
    t: float
    stack: List[str]  # outermost -> innermost


def samples_to_trace(samples: List[Sample]) -> List[Tuple[float, str, str]]:
    if not samples: return []

    results = []

    def _start_trace(t: float, substack: List[str]):
        for name in substack:
            results.append((t, "s", name))
            
    def _end_trace(t: float, substack: List[str]):
        for name in substack[::-1]:
            results.append((t, "e", name))

    _start_trace(samples[0].t, samples[0].stack)

    for idx in range(1, len(samples)):
        prev_sample = samples[idx - 1]
        sample = samples[idx]
        pos = 0
        for a, b in zip(prev_sample.stack, sample.stack):
            if a == b:
                pos += 1
            else:
                break

        _end_trace(sample.t, prev_sample.stack[pos:])
        _start_trace(sample.t, sample.stack[pos:])

    return results

if __name__ == "__main__":
    s2 = [
        Sample(0.0, ['a','b','a','c']),  # a -> b -> a -> c
        Sample(1.0, ['a','a','b','c']),
        Sample(2.0, ['a','a','b','c']),
        Sample(3.0, ['a','a','b','c']),
        Sample(3.0, ['a',]),
        # Sample(2.0, ['a','a','b','c', "e"]),
    ]

    print(samples_to_trace(s2))
