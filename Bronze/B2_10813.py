n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(i+1)

for i in range(m):
    i, j = map(int, input().split())
    temp = lst[i-1]
    lst[i-1] = lst[j-1]
    lst[j-1] = temp

print(*lst)