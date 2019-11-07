a = input("Введите текст")
lower_ = 0
upper_ = 0
for i in a:
    if i.islower():
        lower_ += 1
    else:
        upper_ += 1
print(f"Процент заглавных букв: {upper_/len(a)*100}. Процент прописных чисел: {lower_/len(a)*100}.")