from collections import deque
def execute():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        priority = deque(list(map(int, input().split())))
        value = deque([i for i in range(n)])
        p, v = -1, -1
        tmp = 0
        while True:
            d = max(priority)
            p, v = priority.popleft(), value.popleft()
            if p == d:
                tmp += 1
                if m == v:
                    print(tmp)
                    break
            else:
                priority.append(p)
                value.append(v)
execute()