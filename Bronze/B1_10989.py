import sys
input = sys.stdin.readline
t = int(input())
## Counting Sort
lst = [0] * (10001)
temp = 0
for _ in range(t):
    a = int(input())
    lst[a] += 1
    temp = max(temp, a)
for i in range(temp+1):
    if lst[i] == 0: continue
    for _ in range(lst[i]):
        print(i)