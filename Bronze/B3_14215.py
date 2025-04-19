lst = list(map(int, input().split()))
lst.sort()

if lst[2] >= sum(lst[0:2]):
    print(2*(lst[0]+lst[1])-1)
else: print(sum(lst))
