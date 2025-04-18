a = list(map(int, open(0).read().split()))
print(max(a))
print("%d %d" % (a.index(max(a))//9+1, a.index(max(a))%9+1))