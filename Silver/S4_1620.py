a, b = map(int, input().split())
dic = dict()
dic2 = dict()
for i in range(1, a+1):
    name = input()
    dic[name] = i
    dic2[i] = name
for _ in range(b):
    s = input()
    if s.isdigit():
        print(dic2[int(s)])
    else:
        print(dic[s])