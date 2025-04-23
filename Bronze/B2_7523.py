for i in range(int(input())):
    temp = 0
    a, b = map(int, input().split())
    if a < 0:
        a = abs(a)
        temp = -1*(a)*(a+1)//2 + b*(b+1)//2
    else:
        temp = b*(b+1)//2 - a*(a-1)//2
    print(f"Scenario #{i+1}:\n{temp}\n")