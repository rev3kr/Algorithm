dic = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
       "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
lst = []
for _ in range(3):
    lst.append(input())
print((dic[lst[0]]*10+dic[lst[1]])*(10**dic[lst[2]]))