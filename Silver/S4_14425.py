n, m = map(int, input().split())
lst = set([input() for _ in range(n)])
temp = 0
for _ in range(m):
    s = input()
    if s in lst:
        temp += 1
print(temp)