def execute():
    n = int(input())
    for _ in range(n):
        s = int(input())
        temp = "YES"
        for i in range(2, 10**6+1):
            if s%i == 0: temp = "NO"
        print(temp)
execute()