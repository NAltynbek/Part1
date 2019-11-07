class House:
    def __init__(self, household, total_area):
        self.household = household
        self.total_area = total_area
        self.remaining_area = 0
        self.furniture_list = []


    def add_furniture(self, **kwargs):
        self.remaining_area = self.total_area - sum(kwargs.values())
        self.furniture_list = ', '.join(list(kwargs.keys()))



    def __str__(self):
        res = 'Тип дома: ' + self.household + ', общая площадь: ' + str(self.total_area)
        res += ' кв.м.' + ', свободная площадь ' + str(self.remaining_area)
        res += ' кв.м.' + ', список мебели: ' + self.furniture_list + '.'
        return res

house = House('кирпичный', 10)
house.add_furniture(стол = 1.5, кровать = 4, гардероб = 2)
print(house)
