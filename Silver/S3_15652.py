def execute():
    def back(n, m, depth):
        nonlocal lst

        if depth == m:
            print(*lst)
            return
        else:
            for i in range(n):
                if promising(i, depth):
                    lst[depth] = i+1
                    back(n, m, depth+1)
    
    def promising(i, depth):
        if depth == 0 or lst[depth-1] <= i+1:
            return True
        else: return False

    n, m = map(int, input().split())
    lst = [0 for _ in range(m)]
    back(n, m, 0)
execute()