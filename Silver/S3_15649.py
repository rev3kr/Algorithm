def execute():
    def back(n, m, depth):
        nonlocal lst, visit
        if depth == m:
            print(" ".join(lst))
            return
        else:
            for i in range(n):
                if not visit[i]:
                    visit[i] = True
                    lst[depth] = str(i+1)
                    back(n, m, depth+1)
                    visit[i] = False
    
    n, m = map(int, input().split())
    lst = [0 for _ in range(m)]
    visit = [False for _ in range(n)]
    back(n, m, 0)
execute()