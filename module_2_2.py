first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
print(first, second, third)

if first == third and second == third :
    print('3')
elif first == third or second == third :
    print('1')
else:
    print('0')