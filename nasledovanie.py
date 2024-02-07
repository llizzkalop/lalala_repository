class Car:
    price = 1000000

    def __init__(self,name):
        self.name = name
    def horse_powers(self,powers):
        self.powers = powers
    def __str__(self):
        return '{} {} Количество лошадей:{}, Стоимость : {}'.format(
            self.__class__.__name__,self.name, self.powers, self.price)
class Nissan(Car):
    price = 2500000
    powers = 300
class Kia(Car):
    price = 3000000
    powers = 350

Almera = Nissan(name= 'Almera')
K5 = Kia (name = 'K5')
print(Almera)
print(K5)
