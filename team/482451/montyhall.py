from random import randint

c = 0
list2 = []

while c != 100000:

    p = randint(0, 2)
    list = [0, 0, 0]

    if p == 0:
        list[0] = 1
    elif p == 1:
        list[1] = 1
    else:
        list[2] = 1

    selection = randint(0, 2)
    list.pop(selection)

    if list[0] == 0 and list[1] == 0:
        list2.append(0)

    else:
        list2.append(1)

    c += 1

print(list2 .count(1), '/', c)
print(list2.count(1)/c)
