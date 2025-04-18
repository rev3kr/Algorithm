lst = [True] * 1001
lst[0:2] = [False, False]
for i in range(2, int(1000**0.5)+1):
    if lst[i]:
        for j in range(i*i, 1001, i):
            lst[j] = False

n = int(input())
lst2 = list(map(int, input().split()))
temp = 0
for i in lst2:
    if lst[i]: temp += 1
print(temp)