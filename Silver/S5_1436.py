n = int(input())
i = 666
lst = []
while True:
    if len(lst) == n:
        print(lst[n-1])
        break
    if "666" in str(i):
        lst.append(i)
    i += 1