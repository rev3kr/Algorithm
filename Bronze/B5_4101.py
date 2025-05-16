def execute():
    while True:
        n, m = map(int, input().split())
        if n == m == 0: break
        print("No" if n <= m else "Yes")
execute()