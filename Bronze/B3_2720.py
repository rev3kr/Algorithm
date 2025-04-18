lst = [25, 10, 5, 1]
for _ in range(int(input())):
    c = int(input())
    for i in range(4):
        r, c = c//lst[i], c%lst[i]
        print(r, end = ' ')