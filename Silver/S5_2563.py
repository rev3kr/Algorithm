lst = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a-1, a+9):
        for j in range(b-1, b+9):
            lst[i][j] = 1
temp = 0
for i in range(100):
    for j in range(100):
        if lst[i][j] == 1: temp += 1
print(temp)
