n = int(input())
lst = list(map(int, input().split()))
print(sum(lst)/max(lst)*100/n)