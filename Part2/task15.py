x = int(input("Введите любое число "))
print("Выведены все числа от 1 до",x)
print([i**2 for i in range(1,x+1) if i**2 <= x])




