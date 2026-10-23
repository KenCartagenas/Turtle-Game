import turtle
import utils as util
import flakes as fl
import grasses as gr
import moons as mo
import player as pl

wx, hy = 800, 600
screen = turtle.Screen()
screen.setup(width=wx, height=hy)
screen.bgcolor("#111d37")
pen = turtle.Turtle()
pen.speed(100)
pen.hideturtle()
screen.tracer(0)

rings = [
    (300, "#1a2947"),
    (270, "#202f4e"),
    (240, "#293954"),
    (210, "#34435e"),
    (180, "#414f68"),
    (150, "#E1E6B7"),
    (140, "#ffffff"),
]
moonx, moony = 0, -20
numOfFlakes = 30

moons = mo.Moon(moonx, moony, rings)
flakes = fl.Flakes(numOfFlakes)
grasses = gr.Grasses()
player = pl.Player(screen, 0,0,10,50,"#262153")

moons.draw()
points = [[-wx/2, -25], [wx/2, -25], [wx/2, -hy/2-25], [-wx/2, -hy/2-25]]
pen.pendown()
util.polygon_fill(pen, points, "#000000")
pen.penup()

def animate():
    flakes.update()
    player.update()
    grasses.update()
    screen.update()
    screen.ontimer(animate, 16)
animate()
screen.mainloop()