h, m = map(int, input().split())
time = h*60 + m + int(input())
print("%d %d" % ((time-1440)//60, (time-1440)%60)) if time >= 1440 else print("%d %d" % (time//60, time%60))