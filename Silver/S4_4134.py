t = int(input())
for _ in range(t):
    n = int(input())
    if n < 2:
        print(2)
        continue
    while True:
        temp = True
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                temp = False
                break
        if temp:
            print(n)
            break
        n += 1