from collections import deque
def execute():
    n, k = map(int, input().split())
    queue = deque([int(i) for i in range(1, n+1)])
    lst = []
    while len(queue) != 0:
        for _ in range(k-1):
            queue.append(queue.popleft())
        lst.append(queue.popleft())
    print(f'<{', '.join(map(str, lst))}>')
execute()