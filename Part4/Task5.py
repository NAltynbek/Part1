class Soldier:
    def __init__(self, name):
        self.name = name

class Gun:
    def __init__(self, make='AK47'):
        self.make = make

class Act_of_Shooting(Soldier, Gun):
    def __init__(self, *args):
        Soldier.__init__(self, *args)
        self.bullets = 5

    def fill_bullets(self, num):
        self.bullets += num

    def gun_fire(self):
        if self.bullets:
            print('tigi-tigitishh')
            self.bullets -= 1
        else:
            print('no bullets')

soldier = Act_of_Shooting ('Rayan')
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.fill_bullets(10)
soldier.gun_fire()