temp = 0
for i in input():
    if i in 'ABC': temp += 3
    elif i in 'DEF': temp += 4
    elif i in 'GHI': temp += 5
    elif i in 'JKL': temp += 6
    elif i in 'MNO': temp += 7
    elif i in 'PQRS': temp += 8
    elif i in 'TUV': temp += 9
    else: temp += 10
print(temp)