from turtle import *


def set_body(p_size, radius, extent, bgs):
    for i in range(len(bgs)):
        pencolor(bgs[i])
        pensize(p_size)
        circle(radius, extent)
        circle(-radius, extent)


setup(0.5, 0.75, 400, 100)
penup()
setx(-360)
pendown()
right(50)
bg = ['green', 'blue', 'yellow', 'red', 'pink', 'orange']
set_body(30, 30, 100, bg)
pencolor('black')
circle(30, 130)
circle(20, 100)
forward(20)
fillcolor('yellow')
shape('circle')
shapesize(1)
done()
