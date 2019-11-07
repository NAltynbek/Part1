class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self. odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True

    def land(self):
        self.is_flying = False

    def fly(self, km):
        self.odometer += km

airplane = Airplane('Boing', '737', '2000', '817')
airplane.take_off()
print(airplane.is_flying)
airplane.fly(500)
print(airplane.odometer)
airplane.land()
print(airplane.is_flying)
airplane.fly(500)
print(airplane.odometer)