n  = list(map(int, input("Введите любые числа через пробелы: ").split()))
# n = list(n)
n.sort()
for b in list(n):
    if b % 2 == 0:
        print(b)