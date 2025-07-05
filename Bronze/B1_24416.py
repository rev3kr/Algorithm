def execute():
    n = int(input())
    lst = [0 for _ in range(41)]
    lst[0:3] = [0, 1, 1]
    for i in range(3, 41):
        lst[i] = lst[i-1] + lst[i-2]
    print(f"{lst[n]} {n-2}")
execute()