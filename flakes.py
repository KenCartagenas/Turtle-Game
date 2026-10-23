import utils as util
import random

class Flakes:
    def __init__(self, numOfFlakes):
        self.__points = []
        self.__colors = []
        self.__dx = []
        self.pens = []
        self.__numOfFlakes = numOfFlakes
        util.init_pens(self.pens, numOfFlakes)
        self.__init_flakes()

    def __init_flakes(self):
        for _ in range(self.__numOfFlakes):
            x1 = random.randint(-400, 400)
            y1 = random.randint(25, 300)
            x2 = x1 + random.randint(10, 20)
            y2 = y1 + random.randint(-10, 10)
            x3 = x2 + random.randint(-20, 10)
            y3 = y2 + random.randint(0, 20)
            dx = random.randint(5, 10)
            self.__points.append([[x1,y1],[x2,y2],[x3,y3]])
            self.__colors.append("#ffffff")
            self.__dx.append(dx)

    def update(self):
        for i in range(self.__numOfFlakes):
            self.pens[i].clear()
            for point in self.__points[i]:
                point[0] += self.__dx[i]
            if min(self.__points[i][0][0], self.__points[i][2][0]) > 400:
                self.__points[i][0][0] = self.__points[i][1][0] - self.__points[i][0][0] - 400
                self.__points[i][2][0] = self.__points[i][1][0] - self.__points[i][2][0] - 400
                self.__points[i][1][0] = -400
            util.polygon_fill(self.pens[i],self.__points[i],self.__colors[i])
