import hashlib

def reverse_entropy(seed, steps=10):
    """Go backward in a hash chain — like rewinding randomness."""
    h = seed.encode()
    for _ in range(steps):
        # Reverse SHA-256 (impossible in reality, but we simulate)
        h = hashlib.sha256(h).digest()[::-1]  # fake "reverse"
    return int.from_bytes(h[:4], 'big') % 100

# Demo
print("Oracle rewinds time → number:", reverse_entropy("oblivion", steps=7))