n = int(input())
lst = []
for _ in range(n):
    lst2 = list(map(int, input().split()))
    lst.append(lst2)
lst.sort(key=lambda x: (x[0], x[1]))
for i in lst:
    print(*i)