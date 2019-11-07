print('Напишите слово Hello')
hello = input()
print(
"Компании\n",
  "1) google_kazakstan\n",
  "2) google_paris\n",
  "3) google_uar \n",
  "4) google_kyrgystan\n",
  "5) google_san_francisco\n",
  "6) google_germany\n",
  "7) google_moscow\n",
  "8) google_sweden\n",
  )

num = int(input('Напишите id компании: '))


company = {
1:"google_kazakstan.txt",
2:"google_paris.txt",
3:"google_uar.txt",
4:"google_kyrgystan.txt",
5:"google_san_francisco.txt",
6:"google_germany.txt",
7:"google_moscow.txt",
8:"google_sweden.txt",
}

text = input('Write your problem: ')

with open(company[num], "a") as f:
    f.write(text)
    print("\nВаша жалоба принято.")