n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print("%d %d" % (lst[0], lst[len(lst)-1]))