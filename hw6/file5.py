class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Pencil(Stationery):

    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Handle(Stationery):

    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


if __name__ == '__main__':
    p = Pen()
    n = Pencil()
    h = Handle()
    s = Stationery('канцелярская принадлежность')

    p.draw()
    n.draw()
    h.draw()
    s.draw()
