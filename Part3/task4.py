numbers = input("Введите список чисел через запятую: ").split(" ")
numbers = list(map(int,numbers))
if max(numbers) <= 0:
    print(1)
else:
    for i in range(1, max(numbers)+2):
        if i not in numbers:
            print(i)
            break

        