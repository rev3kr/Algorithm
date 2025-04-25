n = int(input())
dic = dict()
lst = list(map(int, input().split()))
for i in lst:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
m = int(input())
lst2 = list(map(int, input().split()))
for i in lst2:
    print(dic.get(i, 0), end=" ")