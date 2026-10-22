def c_to_f(c):
    return c * 9/5 +32
for c in range(0,101,10):
    print(f"{c:>3}={c_to_f(c):>6.1f}")