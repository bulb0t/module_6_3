from random import randint

class Animal:
    live = True
    sound = None #звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed #скорость передвижения существа

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(" )
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]}')
        print(f'Y: {self._cords[1]}')
        print(f'Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True #наличие клюва

    def lay_eggs(self):
        print(f'"Here are(is) {randint(1, 4)} eggs for you"')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        new_dz = abs(dz) * self.speed / 2
        self._cords[2] -= new_dz

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

db_1 = Duckbill(2)

print(db_1.live)
print(db_1.beak)

db_1.speak()
db_1.attack()

db_1.move(5, 6, 7)
db_1.get_cords()
db_1.dive_in(2)
db_1.get_cords()

db_1.lay_eggs()