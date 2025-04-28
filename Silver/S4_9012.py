import sys
input = sys.stdin.readline

def execute():
    t = int(input())
    for _ in range(t):
        temp = "YES"
        stack = []
        s = input().strip()
        for i in s:
            if i == ')':
                if len(stack) == 0: temp = "NO"
                else: stack.pop()
            else: stack.append(i)
        if len(stack) != 0:
            temp = "NO"
        print(temp)
execute()