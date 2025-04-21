n = int(input())
temp = 10000
for i in range(n//5+1):
    if (n-i*5) % 3 == 0:
        temp = min(temp, i+(n-i*5)//3)
print(-1 if temp == 1001 else temp)