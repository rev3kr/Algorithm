def execute():
    lst = [input() for _ in range(3)]
    a = 0
    for i in range(3):
        if lst[i].isdigit():
            a = int(lst[i])+(3-i)
            break
    if a%3==0 and a%5==0: print("FizzBuzz")
    elif a%3==0: print("Fizz")
    elif a%5==0: print("Buzz")
    else: print(a)
execute()