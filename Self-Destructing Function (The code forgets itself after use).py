import types, sys

def make_oblivion_func(answer):
    def oracle():
        print("Answer:", answer)
        # Delete self from globals
        del sys.modules[__name__].oracle
        print("...function erased from existence.")
    return oracle

# Demo
oracle = make_oblivion_func("The cake is a lie")
oracle()
try:
    oracle()  # NameError!
except NameError as e:
    print("Confirmed:", e)