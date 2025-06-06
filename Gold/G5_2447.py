def execute():
    temp = 0
    def star(x, y, n):
        if n <= 1:
            lst[x][y] = "*"
            return
        m = n // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star(x + i*m, y + j*m, m)
    N = int(input())
    lst = [[' ' for _ in range(N)] for _ in range(N)]
    star(0, 0, N)
    for row in lst:
        print(''.join(row))
execute()