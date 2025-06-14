def execute():

    while True:
        s = input()
        check = True
        if s == "0": break
        
        for i in range(len(s)//2):
            if s[i] != s[-1*i-1]:
                check = False

        print("yes" if check else "no")

execute()