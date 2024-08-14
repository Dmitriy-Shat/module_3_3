def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


value_list = ['string', 8, (2, True, 'кот')]
value_dikt = {'a': False, 'b': (7, True, 'storm'), 'c': 9}
value_list_2 = ['воротник', 54]
#print_params(b = 25) # работает
#print_params(c = [1, 2, 3]) # работает
#print_params(c = 1, 2, 3) # ошибка
print_params(*value_list)
print_params(**value_dikt)
print_params(*value_list_2, 15)