import numpy as np

def fractal_forget(weights, keep=0.3):
    """Erase the *least fractal* weights (toy Mandelbrot-style rule)."""
    flat = weights.flatten()
    # Simple fractal score: escape time of |z^2 + c|
    def escape(c, max_iter=20):
        z = 0
        for i in range(max_iter):
            z = z*z + c
            if abs(z) > 2: return i
        return max_iter

    scores = np.array([escape(abs(w)) for w in flat])
    threshold = np.quantile(scores, keep)       # keep top `keep` fraction
    mask = scores >= threshold
    flat[~mask] = 0.0
    return flat.reshape(weights.shape)

# Demo
w = np.random.randn(5,5)
print("Before:\n", np.round(w,2))
print("After forgetting 70%:\n", np.round(fractal_forget(w, keep=0.3),2))