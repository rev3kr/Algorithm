r, c, zr, zc = map(int, input().split())
lst = []
for _ in range(r):
    s = ""
    s2 = input()
    for i in range(c):
        s += s2[i]*zc
    for _ in range(zr):
        lst.append(s)
for i in lst:
    print(i)