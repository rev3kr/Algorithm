n, t = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(n, 0, -1):
    temp = sum(lst[:i])
    if temp <= t:
        print(i)
        break
    if i == 1:
        print(0)
        break
