def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    print(a, c)
    print(c)
values_dict = {1: 1, 'строка': 2, True: 3}
values_list = [1, 'hello', False]
values_list = print_params(*values_list)
values_dict = print_params(*values_dict)
# не поняла как сделать так, чтобы в конце не писалось None ((
print(print_params())
caca = values_list_2 = {1, 'lalala'}
caca = print_params(*values_list_2)
print(print_params())




