while True:
    timestamps1 = (input('Введите отметку времени в виде чч:мм:сс - '))
    timestamps2 = (input('Введите вторую отметку времени в виде чч:мм:сс - '))
    try:
        [a1, b1, c1] = list(timestamps1.split(':'))
        [a2, b2, c2] = list(timestamps2.split(':'))
        break
    except ValueError:
        print('Ошибка! Неверный формат!')

h1 = int(a1)
h2 = int(a2)
m1 = int(b1)
m2 = int(b2)
s1 = int(c1)
s2 = int(c2)

def hour_per_sec (hour):
    sec_in_hour = hour * 3600
    return sec_in_hour

def min_per_sec (minute):
    sec_in_minute = minute * 60
    return sec_in_minute


sum_seconds1 = hour_per_sec(h1) + min_per_sec(m1) + s1
sum_seconds2 = hour_per_sec(h2) + min_per_sec(m2) + s2

if sum_seconds1 < sum_seconds2:
    print(f'Разница между метками: {sum_seconds2 - sum_seconds1} секунд.')
elif sum_seconds1 == sum_seconds2:
    print('Вы ввели одну и ту же метку!!!')
else:
    print('Ошибка!!! Вторая метка должна быть больше!')