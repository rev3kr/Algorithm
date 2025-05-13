import sys
input = sys.stdin.readline

def execute():
    n, q = map(int, input().split())
    s = set()
    for _ in range(q):
        line = input().split()
        if line[0] == '1':
            s.add(line[1])
        elif line[0] == '2':
            s.discard(line[1])
        else: print(n - len(s))
execute()