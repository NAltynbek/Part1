class Student:
    def __init__(self, fullname, age, major):
        self.fullname = fullname
        self.age = age
        self.major = major

    def __str__(self):
        res = 'name: ' + self.fullname + ', age: '
        res += str(self.age) + ', major: ' + self.major
        return res


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)