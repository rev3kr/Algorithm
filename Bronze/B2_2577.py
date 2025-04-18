import math
lst = list(map(int, open(0).read().split()))
temp = str(math.prod(lst))
for i in range(10):
    print(temp.count(str(i)))