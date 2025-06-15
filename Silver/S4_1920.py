def execute():
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    x = list(map(int, input().split()))
    
    for i in x: print(1 if i in a else 0)

execute()