from collections import deque
import sys
input = sys.stdin.readline
def execute():
    deq = deque([])
    n = int(input())
    for _ in range(n):
        q = len(deq)
        s = input().strip().split()
        if s[0] == '1': deq.appendleft(int(s[1]))
        elif s[0] == '2': deq.append(int(s[1]))
        elif s[0] == '3':
            print(-1 if q==0 else deq.popleft())
        elif s[0] == '4':
            print(-1 if q==0 else deq.pop())
        elif s[0] == '5': print(q)
        elif s[0] == '6':
            print(1 if q == 0 else 0)
        elif s[0] == '7':
            print(-1 if q==0 else deq[0])
        elif s[0] == '8':
            print(-1 if q==0 else deq[-1])
execute()