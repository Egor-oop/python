class Car:
    __speed = 0
    __direction = None

    def __init__(self, speed, color, name, is_police):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = self.__speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        pass

    def show_speed(self):
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    pc = PoliceCar(1200, 'blue', 'a001aa')
    wc1 = WorkCar(12, 'green', 'b012cd')
    wc2 = WorkCar(120, 'green', 'b123cd')
    sc = SportCar(2000, 'rad', 'shumackher')
    tc1 = TownCar(90, 'gray', 'e234fg')
    tc2 = TownCar(60, 'gray', 'e345fg')
    pc.show_speed()
    pc.go()
    pc.show_speed()
    pc.stop()
    print(pc.color)
    pc.go()
    print(pc.name)
    wc1.go()
    wc2.go()
    sc.go()
    tc1.go()
    tc2.go()
    wc1.show_speed()
    wc2.show_speed()
    sc.show_speed()
    tc1.show_speed()
    tc2.show_speed()
