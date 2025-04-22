lst = []
while True:
    n = float(input())
    if n == 999:
        break
    lst.append(n)
for i in range(1, len(lst)):
    print(f"{lst[i]-lst[i-1]:.2f}")