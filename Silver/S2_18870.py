import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst2 = sorted(set(lst))
dic = {value: index for index, value in enumerate(lst2)}
for i in lst:
    print(dic[i], end = " ")