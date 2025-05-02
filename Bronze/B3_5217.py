def execute():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = []
        for i in range(1, n//2+1):
            if i == n-i: continue
            lst.append(f"{i} {n-i}")
        print(f"Pairs for {n}: ", end="")
        print(', '.join(map(str, lst)))
execute()