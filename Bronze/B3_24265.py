lst = [0] * 500001
for i in range(1, 500001):
    lst[i] = lst[i-1] + i
n = int(input())
print(n**2-lst[n])
print(2)