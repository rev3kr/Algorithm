m, n = map(int, input().split())
plist = [True] * (n+1)
plist[0:2] = [False, False]
for i in range(2, int(n**0.5)+1):
    if plist[i]:
        for j in range(i*i, n+1, i):
            plist[j] = False
for i in range(m, n+1):
    if plist[i]:
        print(i)