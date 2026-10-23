import turtle

def circle_fill(p, x, y, radius, color):
    p.goto(x, y-radius)
    p.pendown()
    p.color(color)
    p.begin_fill()
    p.circle(radius=radius)
    p.end_fill()
    p.penup()

def polygon_fill(p, points, color):
    p.goto(points[0][0],points[0][1])
    p.color(color)
    p.pendown()
    p.begin_fill()
    for point in points[1:]:
        p.goto(point)
    p.goto(points[0])
    p.end_fill()
    p.penup()

def init_pens(arr, x):
    for i in range(x):
        p = turtle.Turtle()
        p.speed(0)
        p.penup()
        p.hideturtle()
        arr.append(p)