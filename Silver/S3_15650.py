def execute():

    def back(n, m, depth):
        nonlocal lst, visit

        if depth == m:
            print(*lst)
            return
        else: 
            for i in range(n):
                if check(i, depth):
                    visit[i] = True
                    lst[depth] = i+1
                    back(n, m, depth+1)
                    visit[i] = False

    def check(i, depth):
        nonlocal lst, visit
        if not visit[i] and (depth == 0 or i+1 > lst[depth-1]):
            return True
        else:
            return False

    n, m = map(int, input().split())
    lst = [0 for _ in range(m)]
    visit = [False for _ in range(n)]
    back(n, m, 0)
execute()