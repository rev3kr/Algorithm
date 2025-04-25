a, b = map(int, input().split())
setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))
print(len(setA.difference(setB)) + len(setB.difference(setA)))