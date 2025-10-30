import random

def oblivion_dna(sequence, forget_rate=0.5):
    """Corrupt data in a way that *hides* the original."""
    bits = ''.join(format(ord(c), '08b') for c in sequence)
    flipped = []
    for b in bits:
        if random.random() < forget_rate:
            flipped.append('1' if b == '0' else '0')  # flip
        else:
            flipped.append(b)
    # Reconstruct — but it's *forever changed*
    chars = [chr(int(''.join(flipped[i:i+8]), 2)) for i in range(0, len(flipped), 8)]
    return ''.join(chars)

# Demo
msg = "Secret"
print("Original:", msg)
print("Forgotten:", oblivion_dna(msg, 0.6))