n, m = map(int, input().split())
lst = []
lst2 = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
for _ in range(n):
    lst2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        lst2[i][j] += lst[i][j]
for i in range(n):
    print(*lst2[i])