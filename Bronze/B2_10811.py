n, m = map(int, input().split())
lst = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    lst[i-1:j] = lst[i-1:j][::-1]
print(*lst)