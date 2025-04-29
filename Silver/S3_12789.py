def execute():
    n = int(input())
    stack = []
    lst = list(map(int, input().split()))
    i = 1
    for j in lst:
        while len(stack) != 0 and stack[-1] == i:
            stack.pop()
            i += 1
        if j == i: i += 1
        else: stack.append(j)
    while len(stack) != 0 and stack[-1] == i:
        stack.pop()
        i += 1
    print("Nice" if len(stack)==0 else "Sad")
execute()