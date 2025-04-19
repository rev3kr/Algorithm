lst = []
n = int(input())
for i in range(2,n+1):
    if n == 1: break
    while n%i == 0:
        lst.append(i)
        n //= i
print('' if len(lst) == 0 else '\n'.join(map(str, lst)))