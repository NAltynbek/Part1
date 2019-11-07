class MoneyFmt:

    def __init__(self, data_value):
        self.data_value = data_value
    
    def update(self, new_data):
        self.data_value = new_data

    def __str__(self):
        return self.dollarize()


    def __repr__(self):
        return str(self.data_value)


    def dollarize(self):
        dollar = '${:,.2f}'.format(self.data_value)
        return dollar

a = MoneyFmt(12222.977777)
print(a)
a.update(1333333.67)
print(a)
print(repr(a))