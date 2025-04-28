import sys
from collections import deque
input = sys.stdin.readline

def execute():
    queue = deque([])
    n = int(input())
    for _ in range(n):
        q = len(queue)
        s = input().strip().split()
        if s[0] == "push":
            queue.append(s[1])
        elif s[0] == "pop":
            print(-1 if q==0 else queue.popleft())
        elif s[0] == "size":
            print(q)
        elif s[0] == "empty":
            print(1 if q==0 else 0)
        elif s[0] == "front":
            print(-1 if q==0 else queue[0])
        elif s[0] == "back":
            print(-1 if q==0 else queue[-1])

execute()