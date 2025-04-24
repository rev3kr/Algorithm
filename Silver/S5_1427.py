import sys
input = sys.stdin.readline
s = input().strip()
lst = []
for i in s:
    lst.append(int(i))
lst.sort(reverse=True)
for i in lst:
    print(i, end = "")