def execute():
    def cant(string):
        nonlocal temp
        p = 0; q = len(string)
        l = q // 3       
        if q <= 1:
            temp += string
            return       
        cant(string[p:l])
        temp += " " * l
        cant(string[q-l:q])
    try:
        while True:
            line = input()
            temp = ""
            s = "-" * (3 ** int(line))
            cant(s)
            print(temp)
    except EOFError:
        pass
execute()