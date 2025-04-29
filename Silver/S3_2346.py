from collections import deque
def execute():
    n = int(input())
    lst = list(map(int, input().split()))
    q1 = deque([i for i in range(1, n+1)])
    q2 = deque(lst)
    lst2 = []
    for _ in range(n):
        temp = q2.popleft()
        lst2.append(q1.popleft())
        if len(q1) == 0: break
        if temp > 0:
            temp -= 1
            for _ in range(temp):
                q1.append(q1.popleft())
                q2.append(q2.popleft())
        else:
            for _ in range(abs(temp)):
                q1.appendleft(q1.pop())
                q2.appendleft(q2.pop())
    print(*lst2)
execute()