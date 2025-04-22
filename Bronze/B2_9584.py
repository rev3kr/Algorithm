string = input()
n = int(input())
lst = [input() for _ in range(n)]
lst2 = []
temp = n
for i in range(n):
    lst2.append(lst[i])
    for j in range(9):
        if string[j] == "*": continue
        if string[j] != lst[i][j]:
            lst2.pop()
            temp -= 1
            break
print(temp)
for i in lst2:
    print(i)
