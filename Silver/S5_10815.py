import sys
input = sys.stdin.readline
n = int(input())
lst = set(list(map(int, input().split())))
m = int(input())
lst2 = list(map(int, input().split()))
for i in lst2:
    print(1 if i in lst else 0, end=" ")