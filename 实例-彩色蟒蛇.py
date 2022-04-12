from turtle import *

setup(0.5, 0.75, 400, 100)
penup()
setx(-360)
pendown()
right(50)
l1 = ['green', 'blue', 'yellow', 'red', 'pink']
for i in range(4):
    print(i)
    pencolor(l1[i])
    pensize(20)
    circle(20, 100)
    circle(-20, 100)
pencolor(l1[4])
circle(30, 130)
circle(20, 100)
forward(20)
done()
