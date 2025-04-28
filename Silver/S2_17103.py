t = int(input())
lst = [True] * (10**6 + 1)
lst[0:2] = [False, False]
for i in range(2, int(10**6**0.5)+1):
    if lst[i]:
        for j in range(i*i, 10**6+1, i):
            lst[j] = False
for _ in range(t):
    temp = 0
    n = int(input())
    for i in range(2, n//2+1):
        if lst[i] and lst[n-i]:
            temp += 1
    print(temp)