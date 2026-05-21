 raise RuntimeError("intentional benchmark failure")

import time
import json
import random
from sorter import sort_numbers

data = random.sample(range(100000), 5000)

times = []
for _ in range(5):
    sample = data.copy()
    start = time.perf_counter()
    sort_numbers(sample)
    end = time.perf_counter()
    times.append((end - start) * 1000)

avg_ms = sum(times) / len(times)
throughput = 5000 / (avg_ms / 1000)

with open("artemis_results.json", "w") as f:
    json.dump([
        {
            "execution_time_ms": round(t, 3),
            "throughput_ops_per_sec": round(5000 / (t / 1000), 1),
            "worst_case_ms": round(max(times), 3)
        }
        for t in times
    ], f)

print(f"Avg: {avg_ms:.3f}ms | Throughput: {throughput:.0f} ops/sec")
