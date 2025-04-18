lst = []
for _ in range(5):
    string = list(input())
    if len(lst) < len(string):
        for i in range(len(lst)):
            lst[i] += string[i]
        for i in range(len(lst), len(string)):
            lst.append(string[i])
    else:
        for i in range(len(string)):
            lst[i] += string[i]
for i in lst:
    print(i, end='')