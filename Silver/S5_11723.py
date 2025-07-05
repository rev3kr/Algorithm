import sys
input = sys.stdin.readline
def execute():
    s = set()
    t = int(input())
    for _ in range(t):
        string = input().strip().split()
        if len(string) == 2: num = int(string[1])
        if string[0] == "add": s.add(num)
        elif string[0] == "remove": s.discard(num)
        elif string[0] == "check": print(1 if num in s else 0)
        elif string[0] == "toggle": s.discard(num) if num in s else s.add(num)
        elif string[0] == "all": s = set(i for i in range(1, 21))
        elif string[0] == "empty": s.clear()
execute()