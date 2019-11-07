while True:
    weight_user = (input('Введите cвой вес в кг: '))
    try:
        weight_user = float(weight_user)
        break
    except ValueError:
        print('Ошибка!')

def weight_moon(weight):
    weights = []
    year = 0
    while year <= 15:  
        weights.append((weight + year) * 0.165) 
        year = year + 1 
    return weights

result = weight_moon(weight_user)

print(f'Cейчас ваш вес на Луне будет: {round(result[0], 3)} кг.')
print(f'В следующем году ваш вес на Луне будет: {round(result[1], 3)} кг.')
print(f'Через год ваш вес на Луне будет: {round(result[2], 3)} кг.')
print(f'----- 2 года ваш вес на Луне будет: {round(result[3], 3)} кг.')
print(f'----- 3 года ваш вес на Луне будет: {round(result[4], 3)} кг.')
print(f'----- 4 года ваш вес на Луне будет: {round(result[5], 3)} кг.')
print(f'----- 5 лет ваш вес на Луне будет: {round(result[6], 3)} кг.')
print(f'----- 6 лет ваш вес на Луне будет: {round(result[7], 3)} кг.')
print(f'----- 7 лет ваш вес на Луне будет: {round(result[8], 3)} кг.')
print(f'----- 8 лет ваш вес на Луне будет: {round(result[9], 3)} кг.')
print(f'----- 9 лет ваш вес на Луне будет: {round(result[10], 3)} кг.')
print(f'----- 10 лет ваш вес на Луне будет: {round(result[11], 3)} кг.')
print(f'----- 11 лет ваш вес на Луне будет: {round(result[12], 3)} кг.')
print(f'----- 12 лет ваш вес на Луне будет: {round(result[13], 3)} кг.')
print(f'----- 13 лет ваш вес на Луне будет: {round(result[14], 3)} кг.')
print(f'----- 14 лет ваш вес на Луне будет: {round(result[15], 3)} кг.')