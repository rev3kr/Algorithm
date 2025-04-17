lst = []
for _ in range(10):
    lst.append(int(input())%42)
lst = set(lst)
print(len(lst))