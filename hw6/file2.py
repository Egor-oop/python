class Road:
    WEIGHT1M2 = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, depth):
        return depth * self.WEIGHT1M2 * self._width * self._length


if __name__ == '__main__':
    road_Saratov_Piter = Road(1500, 20)
    print(road_Saratov_Piter.weight(5))
    print(road_Saratov_Piter._length)
    print(road_Saratov_Piter._width)
