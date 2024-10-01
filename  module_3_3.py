def print_params(a=3, b="список", c=True):
    print(a, b, c)


print_params(3, "список", True)
print_params(3, b=25, c=[1, 2, 3])
print_params()

values_list = ('строка', 53, True)
print_params(*values_list)
values_dict = {'a': '  строка', 'b': True, 'c': 8}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)