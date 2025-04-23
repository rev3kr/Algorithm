n, m, k = map(int, input().split())
temp = 300000
grade = 0
for i in range(1, k+1):
    x, y = map(int, input().split())
    if m+1-y+x-1 < temp:
        temp = m+1-y+x-1
        grade = i
print(grade)