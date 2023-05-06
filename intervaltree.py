from typing import List
from random import random, randrange
import time
from intervaltree import Interval, IntervalTree

def rand_key(floor: int, ceiling: int) -> int:
    range_val = ceiling - floor
    return floor + int(range_val * random())

def random_interval(max_start: int, max_length: int, max_stop: int, value: bool) -> Interval:
    start = rand_key(0, max_start)
    stop = min(rand_key(start, start + max_length), max_stop)
    return Interval(start, stop, value)

intervals = []
queries = []

# generate a test set of target intervals
for i in range(10000):
    intervals.append(random_interval(100000, 1000, 100000 + 1, True))

# and queries
for i in range(5000):
    queries.append(random_interval(100000, 1000, 100000 + 1, True))

# using brute-force search
bruteforce_counts = []
t0 = time.time()
for q in queries:
    results = []
    for i in intervals:
        if i.begin >= q.begin and i.end <= q.end:
            results.append(i)
    bruteforce_counts.append(len(results))
t1 = time.time()
print(f"brute force:\t{int((t1 - t0) * 1000)}ms")

# using the interval tree
tree = IntervalTree.from_tuples([(i.begin, i.end, i) for i in intervals])
tree_counts = []
t0 = time.time()
for q in queries:
    results = tree[q.begin:q.end]
    tree_counts.append(len(results))
t1 = time.time()
print(f"interval tree:\t{int((t1 - t0) * 1000)}ms")

# check that the same number of results are returned
for b, t in zip(bruteforce_counts, tree_counts):
    assert b == t
