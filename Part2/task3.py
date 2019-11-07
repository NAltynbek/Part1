num = float(input("Введите число "))
if num %1 == 0:
    num= round(num)
    print((num -1),(num),(num +1))
else:
    print("Введите только целое число!!!")