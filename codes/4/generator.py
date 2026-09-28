import time
import tracemalloc

# Number of elements
N = 1_000_000


# ---------------- LIST-BASED PROCESSING ----------------
def list_processing(n):
    data = [i for i in range(n)]
    result = [x * x for x in data]
    return result


# ---------------- GENERATOR-BASED PROCESSING ----------------
def generator_processing(n):
    for i in range(n):
        yield i * i


# List processing
tracemalloc.start()

start = time.perf_counter()

list_result = list_processing(N)

list_time = time.perf_counter() - start

current, list_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()


# Generator processing
tracemalloc.start()

start = time.perf_counter()

# Process values one at a time
count = 0
total = 0

for value in generator_processing(N):
    total += value
    count += 1

generator_time = time.perf_counter() - start

current, generator_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()


# ---------------- RESULTS ----------------
print("LIST VS GENERATOR PROCESSING")
print("-" * 40)

print(f"Dataset size       : {N:,} elements")

print("\nList-based Processing")
print(f"Execution time     : {list_time:.6f} seconds")
print(f"Peak memory usage  : {list_peak / (1024 * 1024):.2f} MB")

print("\nGenerator-based Processing")
print(f"Execution time     : {generator_time:.6f} seconds")
print(f"Peak memory usage  : {generator_peak / (1024 * 1024):.2f} MB")

print("\nComplexity")
print("List      -> Time: O(n), Space: O(n)")
print("Generator -> Time: O(n), Space: O(1)")