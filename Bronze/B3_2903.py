n = int(input())
lst = [2]
for i in range(15):
    lst.append(2*lst[i]-1)
print(lst[n]**2)