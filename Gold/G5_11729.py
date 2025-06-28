def execute():
    def hanoi(n, start, middle, end):
        if n == 1:
            print(f"{start} {end}")
        else:
            hanoi(n-1, start, end, middle)
            print(f"{start} {end}")
            hanoi(n-1, middle, start, end)
    a = int(input())
    print(2**a-1)
    hanoi(a, 1, 2, 3)
execute()