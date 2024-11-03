def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



values_list = ['one', 2.5, False]
values_dict = {'a': 'first', 'b': 3.5, 'c': False}

values_list_2 = [1, 'True']


print_params(b = 25)
print_params(c = [1,2,3])

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2)
print_params(*values_list_2, 42)