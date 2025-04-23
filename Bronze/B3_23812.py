lst = ["@   @", "@@@@@"]
lst2 = []
n = int(input())
for i in range(5):
    s = ""
    if i%2 == 0:
        for j in range(5):
            s += lst[0][j]*n
        for _ in range(n):
            lst2.append(s)
    else:
        for j in range(5):
            s += lst[1][j]*n
        for _ in range(n):
            lst2.append(s)
for i in lst2:
    print(i)