import math
while True:
    a, b = map(int, input().split())
    if a == b == 0: break
    if math.gcd(a, b) == a: print("factor")
    elif math.lcm(a, b) == a: print("multiple")
    else: print("neither")