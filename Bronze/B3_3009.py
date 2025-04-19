lst = []
for _ in range(3):
    lst.append(list(map(int, input().split())))
lst.sort()
if lst[0][0] == lst[1][0]:
    if lst[0][1] == lst[2][1]: print("%d %d" % (lst[2][0], lst[1][1]))
    else: print("%d %d" % (lst[2][0], lst[0][1]))
else:
    if lst[0][1] == lst[1][1]: print("%d %d" % (lst[0][0], lst[2][1]))
    else: print("%d %d" % (lst[0][0], lst[1][1]))