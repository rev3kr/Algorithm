import math
a, b, c, d, e, f = map(int, input().split())
x = y = 0
if a*d == 0 and b*e == 0:
    if a == 0:
        x = f//d
        y = c//b
    else:
        x = c//a
        y = f//e
elif a*d == 0:
    if a == 0:
        y = c//b
        x = (f - e*y)//d
    else:
        y = f//e
        x = (c - b*y)//a
elif b*e == 0:
    if b == 0:
        x = c//a
        y = (f - d*x)//e
    else:
        x = f//d
        y = (c - a*x)//b
else:
    temp = math.lcm(a, d)
    y = (f*(temp//d)-c*(temp//a))//(e*(temp//d)-b*(temp//a))
    x = (c - (b*y))//a
print(f"{x} {y}")