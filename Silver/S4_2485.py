import math
import functools
n = int(input())
lst = []
lst2 = []
for _ in range(n):
    lst.append(int(input()))
for i in range(1, n):
    lst2.append(lst[i]-lst[i-1])
temp = functools.reduce(math.gcd, lst2)
print(len(range(lst[0], lst[-1]+1, temp)) - n)