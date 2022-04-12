from turtle import *

setup(0.5, 0.75, 400, 100)
pencolor('blue')
begin_fill()
while True:
    fillcolor("red")
    forward(150)
    left(170)
    print(abs(pos()))
    if abs(pos()) < 1:
        break
end_fill()
done()
