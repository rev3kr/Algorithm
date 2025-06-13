def execute():

    def back(n, m, depth):
        nonlocal lst

        if depth == m:
            print(*lst)
            return
        else:
            for i in range(n):
                lst[depth] = i+1
                back(n, m, depth+1)

    n, m = map(int, input().split())
    lst = [0 for _ in range(m)]
    back(n, m, 0)
execute()