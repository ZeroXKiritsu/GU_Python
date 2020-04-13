from time import sleep
# 1
class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
        if i == 0:
            sleep(7)
        elif i == 1:
            sleep(2)
        elif i == 2:
            sleep(5)
        i += 1


trafic = TrafficLight()
trafic.running()
# 2
class Road:
    def __init__(self,length,width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass(self):
        asphalt = self._length * self._width * self.weight * self.height / 1000
        print(f"Для покрытия всего дорожного полотна необходимо {round(asphalt)} массы асфальта")


road = Road(5000,20)
road.mass()
# 3 
class Worker:
    def __init__(self, name, last_name, position, wage, bonus):
        self.name = name
        self.last_name = last_name
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Postion(Worker):
    def __init__(self, name, last_name, position, wage, bonus):
        super().__init__(name, last_name, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.last_name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos = Postion('Kirill', 'Medved', 'QA', 100, 200)
print(pos.get_full_name(), pos.get_total_income())
# 4 
class Car:
    def __init__(self,name,speed,color,is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return  f"The {self.name} went."

    def stop(self):
        return f"\n The {self.name} has stoped"

    def turn(self,direction):
        return  f"\n The {self.name}  turned {direction}"

    def show_speed(self):
        return f"\n You speed is {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\n Your speed is higher than allow! Your speed is {self.speed}"
        else:
            return  f"Speed of {self.name} is normal"

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\n Your speed is higher than allow! Your speed is {self.speed}"
        else:
            return  f"Speed of {self.name} is normal"

class PoliceCar(Car):
    pass

town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())
# 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
