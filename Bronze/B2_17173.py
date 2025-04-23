n, _ = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [False for _ in range(n+1)]
for i in lst:
    for j in range(i, len(lst2), i):
        lst2[j] = True
temp = 0
for i in range(len(lst2)):
    if lst2[i]:
        temp += i
print(temp)