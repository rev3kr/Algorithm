t = int(input())
for _ in range(t):
    h, _, n = map(int, input().split())
    print(f"{n%h:d}{n//h+1:02d}" if n%h!=0 else f"{h:d}{n//h:02d}")