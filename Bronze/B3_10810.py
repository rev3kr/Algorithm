a, b = map(int, input().split())
lst = [0] * a
for _ in range(b):
    i, j, k = map(int, input().split())
    lst[i-1 : j] = [k] * (j-i+1)

print(*lst)