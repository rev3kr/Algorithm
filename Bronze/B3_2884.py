h, m = map(int, input().split())
time = h*60 + m - 45
print("%d %d" % ((time+1440)//60, (time+1440)%60)) if time < 0 else print("%d %d" % (time//60, time%60))