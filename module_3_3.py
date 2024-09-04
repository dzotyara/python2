def print_params(a = 1, b = "строка", c = True):
    print(a,b,c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, "two", 1.1]
values_dict = {'a': 'строка', 'b': 2, 'c': 3.5}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['list', True]
print_params(*values_list_2, 42)