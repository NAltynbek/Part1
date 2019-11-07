"""ПЕРВЫЙ СПОСОБ РЕШЕНИЯ"""
# some_str = input('Введите текст: ').lower()
# if some_str.count('f') == 1:
#     print('У буквы "f" одно вхождение: индекс ' + str(some_str.find('f'))'.')
# elif some_str.count('f') > 1:
#     print('У буквы "f" ' + str(some_str.count('f')) + 
#   ' вхождений. Индекс первого вхождения - ' + 
#   str(some_str.find('f')) + ' , второго - ' + str(some_str.rfind('f')))

"""ВТОРОЙ СПОСОБ РЕШЕНИЯ"""
some_str = list(input('Введите текст: ').lower())
if some_str.count('f') == 1:
    print('У буквы "f" одно вхождение: индекс ' + str(some_str.index('f')))
elif some_str.count('f') > 1:
    print('У буквы "f" ' + str(some_str.count('f')) + 
    ' вхождений. Индекс первого вхождения - ' + str(some_str.index('f')) + 
    ' , второго - ' + str(len(some_str) - 1 - some_str[::-1].index('f')))