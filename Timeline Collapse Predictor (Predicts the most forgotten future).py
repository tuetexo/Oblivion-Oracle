import random
from collections import Counter

def collapse_oracle(options, trials=5000):
    """Which future is *least remembered*?"""
    memories = []
    for _ in range(trials):
        # Simulate a random walk in "timeline space"
        path = [random.choice(options)]
        for _ in range(3):
            path.append(random.choice(options))
        memories.append(tuple(path[-1:]))  # only last state remembered
    # The option that appears *least* = most forgotten = oracle pick
    counts = Counter(m[0] for m in memories)
    return min(counts, key=counts.get)

# Demo
print("Oracle predicts next word:", collapse_oracle(['up', 'down', 'left', 'right']))