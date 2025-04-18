t = int(input())
for _ in range(t):
    temp = 0
    s = list(input().split('X'))
    for i in s:
        temp += sum(range(1, len(i)+1))
    print(temp)