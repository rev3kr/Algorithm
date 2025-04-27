plist = [True] * (123456*2 + 1)
plist[0:2] = [False, False]
for i in range(2, int((123456*2)**0.5)+1):
    if plist[i]:
        for j in range(i*i, 123456*2 + 1, i):
            plist[j] = False
while True:
    n = int(input())
    if n == 0: break
    temp = 0
    for i in range(n+1, 2*n+1):
        if plist[i]:
            temp += 1
    print(temp)