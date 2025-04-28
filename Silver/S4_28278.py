import sys
input = sys.stdin.readline
def execute():
    n1 = int(input())
    stack = []
    for _ in range(n1):
        n = input().split()
        if n[0] == '1': stack.append(int(n[-1]))
        elif n[0] == '2':
            print(-1 if len(stack)==0 else stack.pop())
        elif n[0] == '3': print(len(stack))
        elif n[0] == '4':
            print(1 if len(stack)==0 else 0)
        elif n[0] == '5':
            print(-1 if len(stack)==0 else stack[-1])
execute()