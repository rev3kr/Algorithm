def execute():
    s = input()
    tmp = 0

    for i in range(12):
        if s[i] == "*": continue

        if i%2 == 0: tmp += int(s[i])
        else: tmp += 3*int(s[i])
    tmp += int(s[12])

    for i in range(10):
        if s.index("*")%2 == 0:
            if (tmp+i)%10 == 0:
                print(i)
                break
        else:
            if (tmp+3*i)%10 == 0:
                print(i)
                break

execute()