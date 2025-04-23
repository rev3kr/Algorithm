import sys, heapq
input = sys.stdin.readline
t = int(input())
lst = [int(input()) for _ in range(t)]
heapq.heapify(lst)
lst2 = heapq.nsmallest(t, lst)
for i in lst2:
    print(i)