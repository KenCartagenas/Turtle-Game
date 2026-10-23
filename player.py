import utils as util
import math

class Player:
    w_pressed = False
    s_pressed = False
    a_pressed = False
    d_pressed = False

    def __init__(self, screen, x, y, dx, size, color):
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__dx = dx
        self.__size = size
        self.__color = color
        self.__w_pressed = False
        self.__s_pressed = False
        self.__a_pressed = False
        self.__d_pressed = False
        self.__legoffset = 0
        self.__leg1 = []
        self.__leg2 = []
        self.pens = []

        self.__init_player()
        util.init_pens(self.pens, 6)

    def __press_w(self):
        self.__w_pressed = True

    def __release_w(self):
        self.__w_pressed = False

    def __press_s(self):
        self.__s_pressed = True

    def __release_s(self):
        self.__s_pressed = False

    def __press_a(self):
        self.__a_pressed = True

    def __release_a(self):
        self.__a_pressed = False

    def __press_d(self):
        self.__d_pressed = True

    def __release_d(self):
        self.__d_pressed = False

    def __init_player(self):
        self.__screen.listen()
        self.__screen.onkeypress(self.__press_w, "w")
        self.__screen.onkeyrelease(self.__release_w, "w")
        self.__screen.onkeypress(self.__press_s, "s")
        self.__screen.onkeyrelease(self.__release_s, "s")
        self.__screen.onkeypress(self.__press_a, "a")
        self.__screen.onkeyrelease(self.__release_a, "a")
        self.__screen.onkeypress(self.__press_d, "d")
        self.__screen.onkeyrelease(self.__release_d, "d")
        self.__legoffset = (self.__size//2)*math.sin(45)

    def update(self):
        for i in range(6):
            self.pens[i].clear()
        if self.__w_pressed:
            self.__y += self.__dx
        if self.__s_pressed:
            self.__y += -self.__dx
        if self.__a_pressed:
            self.__x += -self.__dx
        if self.__d_pressed:
            self.__x += self.__dx
        rad = self.__size//2
        util.circle_fill(self.pens[0], self.__x, self.__y, rad, self.__color)
        util.polygon_fill(self.pens[1],[
                        [self.__x-self.__legoffset, self.__y-self.__size//2+self.__legoffset],
                        [self.__x, self.__y-self.__size//2+self.__legoffset],
                        [self.__x, self.__y-self.__size],
                        [self.__x-self.__legoffset, self.__y-self.__size]
                    ], self.__color)
        