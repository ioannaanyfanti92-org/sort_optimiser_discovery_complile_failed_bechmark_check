import time
  import json
  import random
  from sorter import sort_numbers

  # Generate test data — 5000 random numbers
  data = random.sample(range(100000), 5000)

  # Run 5 times and average
  times = []
  for _ in range(5):
      sample = data.copy()
      start = time.perf_counter()
      sort_numbers(sample)
      end = time.perf_counter()
      times.append((end - start) * 1000)  # convert to milliseconds

  avg_ms = sum(times) / len(times)
  throughput = 5000 / (avg_ms / 1000)  # elements per second

  # Write results — Artemis reads this file automatically
  results = {
      "execution_time_ms": round(avg_ms, 3),
      "throughput_ops_per_sec": round(throughput, 1),
      "worst_case_ms": round(max(times), 3)
  }
  with open("artemis_results.json", "w") as f:
      json.dump(results, f)

  print(f"artemis_metric: EXEC_MS: {results['execution_time_ms']}")
  print(f"artemis_metric: THROUGHPUT: {results['throughput_ops_per_sec']}")
  print(f"Avg: {avg_ms:.3f}ms | Throughput: {throughput:.0f} ops/sec")