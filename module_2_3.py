my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
lenList = len(my_list)
a = 0

while a <= lenList:
    b = my_list[a]
    a += 1
    if b >= 1:
        print(b)
    elif b < 0:
        break