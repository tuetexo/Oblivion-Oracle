import weakref

class OblivionCell:
    def __init__(self, value):
        self._value = value
        # Register a callback that wipes the value when the object is GC’d
        weakref.finalize(self, lambda v=value: print(f"Oblivion erased: {v}"))

    def reveal(self):
        return self._value

    def forget(self):
        self._value = None   # manual erase

# Demo
cell = OblivionCell(42)
print("Oracle says:", cell.reveal())
del cell                 # triggers the finalizer → erasure message