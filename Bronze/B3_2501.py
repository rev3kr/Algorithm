lst = []
n, k = map(int, input().split())
for i in range(1, n+1):
    if n%i == 0: lst.append(i)
print(0 if len(lst) < k else lst[k-1])