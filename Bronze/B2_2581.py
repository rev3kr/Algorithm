lst = [True] * 10001
lst[0:2] = [False, False]
for i in range(2, int(10000**0.5)+1):
    if lst[i]:
        for j in range(i*i, 10001, i):
            lst[j] = False

n = int(input()); m = int(input())
temp = 0; temp2 = 0
for i in range(n, m+1):
    if lst[i]:
        temp += i
        if temp2 == 0: temp2 = i
if temp2 == 0: print(-1)
else: 
    print(temp)
    print(temp2)
