lst = []
for _ in range(int(input())):
    s = input()
    if s in lst:
        continue
    lst.append(s)
lst.sort(key=lambda x: (len(x), x))
for i in lst:
    print(i)