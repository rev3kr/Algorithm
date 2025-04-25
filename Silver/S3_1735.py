import math
a, b = map(int, input().split())
c, d = map(int, input().split())
e = a*d + b*c
f = b*d
temp = math.gcd(e, f)
print(f"{e//temp} {f//temp}")