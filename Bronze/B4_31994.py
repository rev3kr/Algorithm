lst = []
for _ in range(7):
    lst.append(list(map(str, input().split())))
for i in range(7):
    lst[i][1] = int(lst[i][1])
list.sort(lst, key=lambda x: x[1])
print(lst[len(lst)-1][0])