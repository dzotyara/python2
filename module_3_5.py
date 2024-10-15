def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) <= 1:
        return first

a_input = input('Введите ваше число: ')

if a_input[0] == '0':
    a_input = '1' + a_input

if a_input[-1] == '0':
    a_input = a_input + '1'

print(a_input)

result = get_multiplied_digits(a_input)
print(result)