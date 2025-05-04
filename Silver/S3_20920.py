import sys
input = sys.stdin.readline
def execute():
    n, m = map(int, input().split())
    dic = dict()
    for _ in range(n):
        s = input().strip()
        if len(s) < m: continue
        if s not in dic: dic[s] = 1
        else: dic[s] += 1
    sorted_s = dict(sorted(dic.items(), key=lambda x: x[0]))
    print(sorted_s)
    sorted_s = dict(sorted(sorted_s.items(), key=lambda item: (item[1], len(item[0])), reverse=True))
    print(sorted_s)
    for k in sorted_s.keys():
        print(k)
execute()