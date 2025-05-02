def execute():
    while True:
        s = input()
        if s == "#": break
        lst = [["%", "%25"],[" ", "%20"],["!", "%21"],["$", "%24"]
               ,["(", "%28"],[")", "%29"],["*", "%2a"]]
        for i in lst:
            s = s.replace(i[0], i[1])
        print(s)
execute()