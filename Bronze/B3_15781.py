def execute():
    n, m = map(int, input().split())
    helmet = set(list(map(int, input().split())))
    jacket = set(list(map(int, input().split())))
    print(max(helmet)+max(jacket))
execute()