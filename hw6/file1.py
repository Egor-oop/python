import time


class TrafficLight:
    COLORS = {'Красный': 7, 'Жёлтый': 2, 'Зелёный': 5}

    __color = None
    __c_index = 0
    change_count = 3

    def __init__(self, init_color='Красный', change_count=3):
        self.__color = init_color if self.COLORS.get(init_color) else list(self.COLORS.keys())[self.__c_index]
        self.__c_index = list(self.COLORS.keys()).index(self.__color)
        self.change_count = change_count

    def running(self):
        print(self.__color)
        while self.change_count:
            time.sleep(self.COLORS.get(self.__color))
            self.__c_index = (self.__c_index + 1) % 3
            self.__color = list(self.COLORS.keys())[self.__c_index]
            print(self.__color)
            self.change_count -= 1


if __name__ == '__main__':
    while True:
        change_count = 3
        try:
            change_count = int(change_count)
            break
        except ValueError as e:
            print('Ожидаем целое число')
    lights = TrafficLight('Зеленый', change_count)
    lights.running()
