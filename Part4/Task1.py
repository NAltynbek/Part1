class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
    
    def get_student_info(self):
        print(f'{self.name} {self.lastname} поступил  {self.year_of_entrance} г. на факультет: {self.department}.')

student1 = Student('Орозбай', 'Маданбек уулу', 'Программирование', '2009')
student1.get_student_info()