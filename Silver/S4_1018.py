lst = ["BWBWBWBW", "WBWBWBWB"]
n, m = map(int, input().split())
lst2 = []
for _ in range(n):
    lst2.append(input())
temp = 50*50+1
for i in range(0, n-7):
    for j in range(0, m-7):
        temp2 = 0
        for k in range(i, i+8):
            temp2 += sum(c1 != c2 for c1, c2 in zip(lst[(i+k)%2], lst2[k][j:j+8]))
        temp = min(temp, min(temp2, 64-temp2))
print(temp)