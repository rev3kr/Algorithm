while True:
    temp = 1
    lst = list(map(int, input().split()))
    if lst[0] == 0: break
    for i in range(1, len(lst)):
        temp = temp*lst[i] if i%2==1 else temp-lst[i]
    print(temp)