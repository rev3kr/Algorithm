import sys
input = sys.stdin.readline
def execute():
    n = int(input())
    temp = 0
    chat = set()
    for _ in range(n):
        s = input().strip()
        if s == "ENTER":
            chat.clear()
            continue
        if s in chat:
            continue
        temp += 1
        chat.add(s)
    print(temp)
execute()