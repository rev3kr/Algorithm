lst = [i+1 for i in range(30)]
for _ in range(28):
    lst.pop(lst.index(int(input())))

print('\n'.join(map(str, lst)))