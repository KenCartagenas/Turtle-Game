import utils as util
import random

class Grasses:
    def __init__(self):
        self.__points = []
        self.__colors = []
        self.__dx = []
        self.pens = []
        self.__numOfGrass = 0

        self.__init_grasses()

    def __init_grasses(self):     
        start_row = -50
        offsety = 50
        width = 0
        for _ in range(5):
            while width < 800:
                offsetx = random.randint(-20,+10)
                p1 = [-400+width+offsetx,start_row]
                grass_height = random.randint(70,150)
                grass_width = random.randint(20,30)
                width += grass_width
                p2 = [p1[0]+grass_width,start_row]
                p3 = [random.randint(p1[0], p2[0]),grass_height+start_row]
                color = random.choice(["#0a1420", "#0c1928", "#102033", "#132438", "#172a40"])
                self.__points.append([p1,p2,p3])
                self.__colors.append(color)
                self.__dx.append(1)
                util.init_pens(self.pens, 1)
                self.__numOfGrass += 1
            width = 0
            start_row -= offsety

    def update(self):
        for i in range(self.__numOfGrass):
            self.pens[i].clear()
            if self.__points[i][2][0] > self.__points[i][1][0] or self.__points[i][2][0] < self.__points[i][0][0]:
                self.__dx[i] *= -1
            self.__points[i][2][0] += self.__dx[i]
            util.polygon_fill(self.pens[i],self.__points[i],self.__colors[i])