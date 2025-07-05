def execute():
    t = int(input())
    lst = [[0, 0] for _ in range(41)]
    lst[0][0] = 1; lst[1][1] = 1
    for i in range(2, 41):
        lst[i][0], lst[i][1] = lst[i-1][0] + lst[i-2][0], lst[i-1][1] + lst[i-2][1]
    for _ in range(t):
        n = int(input())
        print(*lst[n])
execute()