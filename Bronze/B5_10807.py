n = int(input())
lst = list(map(int, input().split()))
v = int(input())
temp = 0
for i in lst:
    if i == v:
        temp += 1
print(temp)