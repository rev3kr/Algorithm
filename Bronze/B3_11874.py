def execute():
    l = int(input())
    d = int(input())
    x = int(input())
    for i in range(l, d+1):
        temp = 0
        for j in str(i):
            temp += int(j)
        if temp == x:
            print(i)
            break
    for i in range(d, l-1, -1):
        temp = 0
        for j in str(i):
            temp += int(j)
        if temp == x:
            print(i)
            break
execute()