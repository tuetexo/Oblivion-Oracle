import random
import cmath   # complex numbers = “imaginary time”

def oblivion_oracle(target, trials=10_000):
    """Predict the *most forgotten* outcome of a dice roll."""
    # 1-6 dice, we want to “guess” the target
    forgotten = []
    for _ in range(trials):
        # imaginary time step: rotate phase by random angle
        t = cmath.exp(1j * random.uniform(0, 2*3.1416))
        # simulated “timeline that never happened”
        roll = 1 + int((t.imag * 6) % 6)
        if roll == target:
            # the timeline is *forgotten* (phase → 0)
            forgotten.append(abs(t))
    # the answer that survived the least = most forgotten
    return target if forgotten else random.randint(1,6)

# Demo
print(oblivion_oracle(4))