lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))
x = max(lst)[0] - min(lst)[0]
y = max(lst, key=lambda i: i[1])[1] - min(lst, key=lambda i: i[1])[1]
print(x*y)