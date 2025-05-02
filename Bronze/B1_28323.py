def execute():
    n = int(input())
    lst = list(map(int, input().split()))
    odd = even = 0
    temp = True
    for i in lst:
        if i%2 == 1 and temp:
            odd += 1
            temp = False
        elif i%2 == 0 and not temp:
            odd += 1
            temp = True
    temp = True
    for i in lst:
        if i%2 == 0 and temp:
            even += 1
            temp = False
        elif i%2 == 1 and not temp:
            even += 1
            temp = True
    print(max(odd, even))
execute()