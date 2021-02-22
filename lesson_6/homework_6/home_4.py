"""
Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:

    def __init__(self, name, color, speed, is_police = False):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = is_police

    def car_go(self):
        return f'{self.name} поехала.'

    def car_stop(self):
        return f"\n {self.name} остановилась."

    def car_turn(self, direction):
       return f"/n {self.name} повернула {direction}."

    def show_speed(self):
        return f"/n Ваша скорость {self.speed}."

class TownCar(Car):


    def show_speed(self):
        def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f" Наблюдатся превышение скорости. Ваша скорость {self.speed}."
        else:
            return f" Ваша скорость {self.speed} в пределах нормы."

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f" Cкорость {self.speed}."

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f" Наблюдатся превышение скорости. Ваша скорость {self.speed}."
        else:
            return f" Ваша скорость {self.speed} в пределах нормы."

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f" Cкорость {self.speed}."


town = TownCar("Ford","metallic", 100, False)
print(town.car_go(), town.show_speed(), town.car_turn("left"), town.car_stop())

sport = SportCar("Audi R8", "red", 200, False)
print(sport.car_go(), sport.show_speed(), sport.car_turn("right"), sport.car_stop())

work = WorkCar("VAZ", "black", 30, False)
print(work.car_go(), work.show_speed(), work.car_turn("left"), work.car_turn("right"), sport.car_stop())

polise = PoliceCar("Patriot", "brawn", 120, True)
print(polise.car_go(), polise.show_speed(), polise.car_turn("left"), polise.car_stop())
