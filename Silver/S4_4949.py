import sys
input = sys.stdin.readline

def execute():
    while True:
        stack = []
        s = input()
        temp = True
        if s == '.\n': break
        for i in range(len(s)):
            if s[i] in ('(', '['):
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0:
                    temp = False
                    break
                if stack[-1] == '(':
                    stack.pop()
                else:
                    temp = False
                    break
            elif s[i] == ']':
                if len(stack) == 0:
                    temp = False
                    break
                if stack[-1] == '[':
                    stack.pop()
                else:
                    temp = False
                    break
        if temp and len(stack) != 0:
            temp = False
        print("yes" if temp else "no")
execute()
