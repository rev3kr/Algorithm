n = int(input())
temp = 0
n -= 3
for i in range(1, n+1):
    temp += i*n*(n+1)//2
    n -= 1
print(temp)