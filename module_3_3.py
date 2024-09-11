def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_dict = {'a' : 1, 'b' : False, 'c' : "3"}
values_list = [1, 'Hellow', 1.25]

print_params(**values_dict)
print_params(*values_list)

values_list_2 = [123, False]
print_params(*values_list_2
