n = int(input())
lst = [list(map(str, input().split())) for _ in range(n)]
lst.sort(key=lambda x: int(x[0]))
for i in lst:
    print(*i)