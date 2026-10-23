import utils as util

class Moon:
    def __init__(self, x, y, rings):
        self.pens = []
        self.__x = x
        self.__y = y
        self.__rings = rings
        util.init_pens(self.pens, 7)

    def draw(self):
        i = 0
        for radius, color in self.__rings:
            util.circle_fill(self.pens[i], self.__x, self.__y, radius, color)
            i += 1